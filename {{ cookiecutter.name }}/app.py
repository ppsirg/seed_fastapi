from fastapi import FastAPI


app = FastAPI(
    title="{{ cookiecutter.name }}", description="{{ cookiecutter.description }}"
)


@app.get("/")
def initial_service():
    return "not implemented"
