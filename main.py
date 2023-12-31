from typing import List

from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


# @app.get('/')
# async def home():
#     return {'key': 'Hello'}
#
#
# @app.get('/{pk}')
# async def get_item(pk: int, q: int = None):
#     return {'key': pk, 'q': q}
#
#
# @app.get('/user/{pk}/items/{item}/')
# async def get_user_item(pk: int, item: str):
#     return {'user': pk, 'item': item}


@app.post('/book')
async def create_book(item: Book):
    return item


@app.get('/book')
async def get_book(q: List[str] = Query(['test', 'test2'], description='Search book')):
    return q
