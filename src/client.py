from __future__ import annotations
import chat_pb2_grpc, chat_pb2
import asyncio
import grpc.aio


async def amain():
    async with grpc.aio.insecure_channel("127.0.0.1:50050") as channel:
        stub = chat_pb2_grpc.GreeterStub(channel)
        response: chat_pb2.Response = await stub.Greet(chat_pb2.Request(name="World"))
        print(response.greeting)


def main():
    asyncio.run(amain())
