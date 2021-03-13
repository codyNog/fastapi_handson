import dataclasses

from fastapi import FastAPI
from use_cases.user_repository import UserRepository
from impl.user_repository import UserRepositoryImpl
from use_cases.property_repository import PropertyRepository
from impl.property_respository import PropertyRepositoryImpl
from routers.user import user_router
from routers.property import property_router


@dataclasses.dataclass()
class Backend:
    user_repos: UserRepository = UserRepositoryImpl()
    property_repos: PropertyRepository = PropertyRepositoryImpl()


backend = Backend()
app = FastAPI()

app.include_router(
    user_router
)
app.include_router(
    property_router
)


@app.get("/")
async def root():
    # TODO 適当な文字列をprintする
    # print("モルカー")

    # print(requests.get("http://sample-httpbin.sample/ip").text)
    return backend.user_repos.get_users()
