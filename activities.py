import dataclasses
from temporalio import activity


@dataclasses.dataclass
class Params:
    test_phrase: str
    model_id: str


@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"


@activity.defn
async def run_simulation(params: Params):
    return params.test_phrase