import asyncio

async def answer_calls():
    while True:
        print("Отвечаю на телефонные звонки")
        await asyncio.sleep(2)

async def welcome_visitors():
    while True:
        print("Принимаю посетителей")
        await asyncio.sleep(3)

async def book_flight_tickets():
    while True:
        print("Пытаюсь забронировать билеты на самолет")
        await asyncio.sleep(5)

async def control_meeting_schedules():
    while True:
        print("Контролирую графики встреч")
        await asyncio.sleep(1)

async def fill_documents():
    while True:
        print("Заполняю документы")
        await asyncio.sleep(4)

async def secretary():
    tasks = [
        answer_calls(),
        welcome_visitors(),
        book_flight_tickets(),
        control_meeting_schedules(),
        fill_documents()
    ]

    await asyncio.gather(*tasks)

asyncio.run(secretary())
