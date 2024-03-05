from fastapi import FastAPI
import uvicorn
from pydantic import EmailStr, BaseModel

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello():
    return [
        "message like this"
    ]


@app.get("/hello/")
def hello_name(name: str, surname: str):
    name = name.title()
    surname = surname.title()
    return {
        "message": f"Hey, {name} {surname}"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

