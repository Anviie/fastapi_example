from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

hotels = [
    {'id': 1, 'title': 'Sochi'},
    {'id': 2, 'title': 'Dubai'},
]

@app.get('/hotels')
def get_hotels(
    id: int | None = Query(None, description='Уникальный идентификатор'),
    title: str | None = Query(None, description='Название отеля'),
):
    
    return [hotel for hotel in hotels if hotel['title'] == title and hotel['id'] == id]

@app.get('/')
def main():
    return [{'Boba':1}, {'Goga': 2}]


if __name__ == '__main__':
    uvicorn.run('example_api:app', reload=True)