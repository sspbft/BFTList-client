"""Example client shell used to send requests to all BFTList nodes."""


import asyncio
from comm import build_payload, broadcast

ops = ["NO_OP", "APPEND"]

async def main():
    print("Welcome to BFT Client shell! Available operations are 'NO_OP' and APPEND x")
    while True:
        s = input("BFTList Client > ")
        parts = s.split(" ")
        op = parts[0]
        if op not in ops:
            print(f"Illegal operation {op}")
        if len(parts) == 2:
            payload = build_payload(0, op, parts[1])
        else:
            payload = build_payload(0, op)
        await broadcast(payload)

# if __name__ == '__main__':
asyncio.run(main())
