import os
from fastapi import FastAPI
# import requests

app = FastAPI()

FOO = os.getenv("FOO", "set FOO as an environment variable to change me")

@app.get("/")
async def root():
    print(FOO)
    # print(requests.get("http://sample-httpbin.sample/ip").text)
    return {"message": "hoge"}
