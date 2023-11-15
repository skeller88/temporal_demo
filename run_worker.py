import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from activities import run_simulation, say_hello
from config import simulations_task_queue
from workflows import RunSimulation, SayHello


# async def main():
#     client = await Client.connect("localhost:7233", namespace="default")
#     # Run the worker
#     worker = Worker(
#         client, task_queue="hello-task-queue", workflows=[SayHello], activities=[say_hello]
#     )
#     await worker.run()

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue=simulations_task_queue, workflows=[RunSimulation], activities=[run_simulation]
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
