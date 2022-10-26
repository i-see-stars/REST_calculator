from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.calc import Calculator


calc_obj = Calculator()

app = FastAPI()


class MyCustomException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(MyCustomException)
# async def MyCustomExceptionHandler(request: Request, exception: MyCustomException):
async def my_custom_exception_handler(request: Request, exception: MyCustomException):
    return JSONResponse(
        status_code=400, content={"message": "POST request. Error occured."}
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.get("/", response_class=PlainTextResponse)
@app.get("/index", response_class=PlainTextResponse)
async def root():
    return "Hello world"


@app.get("/eval/{phrase:path}", response_class=PlainTextResponse, status_code=200)
async def eval_func(phrase: str):
    phrase_ = str(calc_obj.solve(phrase))
    result = phrase + " = " + phrase_
    # Some mock condition for testing purposes.
    if result == "1+2 = 3":
        raise HTTPException(
            status_code=400, detail="GET request. Mock condition met. Evaluation error!"
        )

    elif result == "1+3 = 4":
        raise MyCustomException(name=result)

    return result


@app.post("/eval/{phrase:path}", status_code=201)
async def eval_func_post(phrase: str):
    phrase_ = str(calc_obj.solve(phrase))
    result = phrase + " = " + phrase_

    if result == "1+3 = 4":
        raise MyCustomException(name=result)

    return {"response": result}
