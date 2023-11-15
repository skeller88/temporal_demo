import asyncio
import dataclasses
from datetime import timedelta
from typing import List

from temporalio import workflow

from activities import run_simulation, Params


# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import say_hello


@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=5)
        )


@dataclasses.dataclass
class WorkflowParams:
    test_phrases: List[str]
    model_id: str


@workflow.defn
class RunSimulation:
    @workflow.run
    async def run(self, params: WorkflowParams) -> List[str]:
        results = []
        for test_phrase in params.test_phrases:
            result = await workflow.execute_activity(
                run_simulation, Params(test_phrase=test_phrase, model_id=params.model_id), start_to_close_timeout=timedelta(seconds=5)
            )
            results.append(result)

        return results
