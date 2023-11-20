import asyncio


async def Plus(a, b):
    print('складывание началось')
    await asyncio.sleep(2)
    print('результат суммы: ', a + b)
    return a + b

async def kvadrat(a):
    print('Квадрацированние началось')
    await asyncio.sleep(2)
    print('результат квадрацирования: ', a**2)
    return a **2

async def main():
    task1 = asyncio.create_task(Plus(4, 4))
    task2 = asyncio.create_task(kvadrat(4))

    await asyncio.gather(task1, task2)

asyncio.run(main())