import os

from fastapi import FastAPI

# import requests

app = FastAPI()

MESSAGE = os.getenv("MESSAGE", "set MESSAGE as an environment variable to change me")


@app.get("/")
async def root():
    # TODO 適当な文字列をprintする
    # print("モルカー")

    # print(requests.get("http://sample-httpbin.sample/ip").text)
    return {"message": MESSAGE}
