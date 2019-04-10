"""Example client shell used to send requests to all BFTList nodes."""


import asyncio
from comm import build_payload, broadcast

ops = ["NO_OP"]

async def main():
    print("Welcome to BFT Client shell! Available operations are 'NO_OP'")
    while True:
        s = input("BFTList Client > ")
        if s not in ops:
            print(f"Illegal operation {op}")
            continue
        payload = build_payload(0)
        await broadcast(payload)

# if __name__ == '__main__':
asyncio.run(main())
