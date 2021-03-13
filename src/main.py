import dataclasses

from fastapi import FastAPI
from use_cases.user_repository import UserRepository
from impl.user_repository import UserRepositoryImpl
from routers.user import user_router


@dataclasses.dataclass()
class Backend:
    user_repos: UserRepository = UserRepositoryImpl()


backend = Backend()
app = FastAPI()

app.include_router(
    user_router,
)


@app.get("/")
async def root():
    # TODO 適当な文字列をprintする
    # print("モルカー")

    # print(requests.get("http://sample-httpbin.sample/ip").text)
    return backend.user_repos.get_users()
