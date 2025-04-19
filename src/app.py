from fastapi import FastAPI, Query, Request
from fastapi.datastructures import URL, QueryParams
from fastapi.params import Header
from fastapi.responses import FileResponse, RedirectResponse
from api.v1.auth import router as auth_router
from uvicorn import run as uvicorn_run


app = FastAPI()

app.include_router(auth_router)


@app.get("/", status_code=200)
async def get_main_page():
    return FileResponse("src/index.html")


if __name__ == "__main__":
    uvicorn_run("app:app", reload=True)
