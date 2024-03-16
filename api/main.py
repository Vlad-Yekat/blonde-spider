from fastapi import FastAPI, Body
import spider_api

app = FastAPI()
app.include_router(spider_api.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=8002)
