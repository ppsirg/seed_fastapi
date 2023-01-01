from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import CORS


app = FastAPI(
    title="{{ cookiecutter.name }}", description="{{ cookiecutter.description }}"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS.ORIGINS,
    allow_credentials=CORS.CREDENTIALS,
    allow_methods=CORS.METHODS,
    allow_headers=CORS.HEADERS,
)

## routers ##


@app.get("/")
def initial_service():
    return "not implemented"
