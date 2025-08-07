from fastapi import FastAPI
import uvicorn
import time
import asyncio
import threading

app = FastAPI()

hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'voc'},
    {'id': 2, 'title': 'Dubai', 'name': 'bok'},
]


@app.get('/sync/{id}')
def sync(id: int):
    print(f'sync Begin {id} | Thread use: {threading.active_count()}')
    time.sleep(3)
    # print(f'sync End {id}')

@app.get('/async/{id}')
async def a_sync(id: int):
    print(f'async Begin {id} | Thread use: {threading.active_count()}')
    await asyncio.sleep(3)
    # print(f'async End {id}')

@app.get('/')
def main():
    return 'Стартовая сраница'

if __name__ == '__main__':
    uvicorn.run('async_vs_sync_api:app', reload=False, workers=10)
    