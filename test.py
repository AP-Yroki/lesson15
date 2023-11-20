import asyncio
import httpx

# async def async_func(task_no):
#     print(f'{task_no}: Запуск...')
#     await asyncio.sleep(1)
#     print(f'{task_no}... Готово!')
#
# async def main():
#     taskA = asyncio.create_task(async_func('taskA'))
#     taskB = asyncio.create_task(async_func('taskB'))
#     taskC = asyncio.create_task(async_func('taskC'))
#     await asyncio.wait([taskA, taskB, taskC])
#
# if __name__ == '__main__':
#     asyncio.run(main())


# async def count(counter):
#     print(f'Количество записей в цикле: {len(counter)}')
#     while True:
#         await asyncio.sleep(1 / 1000)
#         counter.append(1)
#
# async def print_every_sec():
#     while True:
#         await asyncio.sleep(1)
#         print(f' - 1 секунда прошла.')
#
# async def print_every_5_sec():
#     while True:
#         await asyncio.sleep(5)
#         print(f'----- 5 cекунд прошло')
#
# async def print_every_10_sec():
#     while True:
#         await asyncio.sleep(10)
#         print(f'----- 10 cекунд прошло')
#
# async def main():
#
#     task1 = asyncio.create_task(count([]))
#     task2 = asyncio.create_task(print_every_sec())
#     task3 = asyncio.create_task(print_every_5_sec())
#     task4 = asyncio.create_task(print_every_10_sec())
#
#     await asyncio.gather(task1, task2, task3, task4)
#
#
# asyncio.run(main())


# async def brewCoffee():
#     print('Start brewCoffee()')
#     await asyncio.sleep(3)
#     print('End brewCoffee()')
#     return 'Coffee ready'
#
# async def toastBage1():
#     print('start toastBage1()')
#     await asyncio.sleep(2)
#     print('End toastBage1()')
#     return 'Bage1 toasted'
#
# async def main():
#     start_time = time.time()
#
#     batch = asyncio.gather(brewCoffee(), toastBage1())
#     result_coffee, result_bage1 = await batch
#
#     end_time = time.time()
#     spent_time = end_time - start_time
#     print(f'Result of brewCoffee: {result_coffee}')
#     print(f'Result of toastBage1: {result_bage1}')
#     print(f'Total execution time: {spent_time:.2f} seconds')
#
# asyncio.run(main())

async def download(current_activity):
    url = f'https://reqres.in/api/users/{current_activity}'

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            _r = r.json()
            r_dict = _r.get("data")
            print(r_dict["first_name"])
        else:
            print(r.status_code)
        print(f"Показываю: {current_activity}")

async def main():
    page_count = int(input('Сколько людей нужно?: '))

    current_activity = 0
    while current_activity < page_count:
        current_activity += 1
        await download(current_activity)
    print('Done')

asyncio.run(main())

