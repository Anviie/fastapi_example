from fastapi import FastAPI, Query, Request, Body, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn


app = FastAPI() # Главный обьект, без него не как
templates = Jinja2Templates(directory='templates') # html Вёрстка


class Hotel(BaseModel):
    tile: str
    name: str


class PatchHotel(BaseModel):
    title: str | None = None
    name: str | None = None


# Псевдо данные из БД
hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'voc'},
    {'id': 2, 'title': 'Dubai', 'name': 'bok'},
]


@app.get('/hotels')
def get_hotels(
    id: int | None = Query(None, description='Уникальный идентификатор'),
    title: str | None = Query(None, description='Название отеля'),
):
    if id == None or title == None: return hotels # All return
    return [hotel for hotel in hotels if hotel['title'] == title and hotel['id'] == id] # returns the result with the condition

@app.delete('/hotels/{hotel_id}')
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}

@app.post('/hotels') # Что бы получить данные из тела сообщения, строим из входящей переменной обьект Body / embed - делает из строки json (ключ - переменная / значение input)
def create_hotel(create_field: Hotel):
    global hotels
    id_max = max([i['id'] for i in hotels]) + 1
    hotel_dict = {'id': id_max, **create_field.model_dump()}
    hotels.append(hotel_dict)
    return 'Success'

@app.put('/hotels/{id}') # Изменение всех параметров за исключение ID (возможно обработать только при предоставлении всех параметров)
def put_hotels(id: int, update_field: Hotel = Body()):
    global hotels
    for enum, i in enumerate(hotels):
        if i['id'] == id:
            updated_hotel = {"id": id, **update_field.model_dump()}
            hotels[enum] = updated_hotel
            return 'Success'

@app.patch('/hotels/{id}')  # Изменение ограниченного кол-ва параметров (>= 1) за исключением ID
def patch_hotels(
    id: int = Path(description='ID'),
    update_field: PatchHotel = Body()
    ):
    global hotels
    for i in hotels:
        if i['id'] == id:
            i.update(update_field.model_dump(exclude_unset=True))
            return 'Success'

# Корневой маршрут
@app.get('/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request}) # Маршрут для html


if __name__ == '__main__':
    uvicorn.run('example_api:app', reload=True)