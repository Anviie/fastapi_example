hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'voc'},
    {'id': 2, 'title': 'Dubai', 'name': 'bok'},
]

# next((i.keys() for i in hotels))

# print(
#     *[i for i in hotels[0]]
# )

# hotels[0].update({'id':1, 'title': 'Boba'})
# print(hotels)

# id_max = max([i['id'] for i in hotels]) + 1
# print(id_max)

import asyncio
import aiohttp
import time

async def get_http_data(i: int, endpoint: str):
    url = f'http://127.0.0.1:8000/{endpoint}/{i}'
    async with aiohttp.ClientSession() as sessions:
        async with sessions.get(url) as responce:
            # print(f'END - {i} - {responce.status}')
            ...
            
async def main():
    await asyncio.gather(
        *[get_http_data(i,'async') for i in range(3000)]
        # *[get_http_data(i,'sync') for i in range(3000)]
        )
    
    
if __name__ == '__main__':
    begin_time = time.time()
    asyncio.run(main())
    print(
        time.time() - begin_time
    )