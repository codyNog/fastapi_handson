from fastapi import FastAPI
# import requests

app = FastAPI()


@app.get("/")
async def root():
    # print(requests.get("http://sample-httpbin.sample/ip").text)
    return {"message": "hoge"}
