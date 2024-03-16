from typing import Union
import asyncio
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi import APIRouter
from api.models.spiders import Spider
# from api.service import create_spider
from api.fixtures.spiders import get_one_fixture, get_all_fixtures

app = FastAPI()

# router = APIRouter(prefix = "/api")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items2")  # so, in query paramaters
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/hi")
async def greet(who:str = Body(embed=True)):
    return f"Hello? {who}?"


@app.get('/spiders/{spider_id}', response_model=Spider)
async def get_one(spider_id: int) -> Spider:
    # tag: Spider = service.get(tag_str)
    one_spider = get_one_fixture(spider_id)
    return one_spider

@app.get('/spiders/')
async def get_all_spiders() -> list[Spider]:
    list_of_spiders = get_all_fixtures()
    return list_of_spiders

# @app.post("/")
# async def post_spider(spider: Spider) -> Spider:
#     return create_spider(spider)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_api:app", reload=True, port=8002)