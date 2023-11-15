import asyncio
import random

from temporalio.client import Client

from activities import Params
from config import simulations_task_queue
from workflows import RunSimulation, SayHello, WorkflowParams


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        RunSimulation.run, WorkflowParams(test_phrases=["a", "b"], model_id="m1"), id=str(random.random()),
        task_queue=simulations_task_queue
    )
    # Execute a workflow
    # result = await client.execute_workflow(
    #     SayHello.run, "Temporal", id="hello-workflow", task_queue="hello-task-queue"
    # )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
