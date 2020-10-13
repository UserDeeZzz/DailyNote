import asyncio
import select

async def main():
    await asyncio.sleep(1)
    print("end...")

select(3)
asyncio.get_event_loop()
asyncio.run(main())
