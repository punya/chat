import chat_pb2_grpc, chat_pb2
import asyncio
import grpc.aio

class Greeter(chat_pb2_grpc.GreeterServicer):
    async def Greet(self, request: chat_pb2.Request, context: grpc.aio.ServicerContext):
        return chat_pb2.Response(greeting=f'Hello, {request.name}!')


async def amain():
    server = grpc.aio.server()
    server.add_insecure_port('127.0.0.1:50050')
    chat_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    await server.start()
    await server.wait_for_termination()

def main():
    asyncio.run(amain())
