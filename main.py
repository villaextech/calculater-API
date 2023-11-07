from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

class CalculationRequest(BaseModel):
    operation: str
    num1: float
    num2: float

@app.post("/Add")
def add_numbers(request: CalculationRequest):
    result = request.num1 + request.num2
    return {"result": result}

@app.post("/Subtract")
def subtract_numbers(request: CalculationRequest):
    result = request.num1 - request.num2
    return { "result":result }

@app.post("/Multiply")
def multiply_numbers(request: CalculationRequest):
    result = request.num1 * request.num2
    return { "result": result }

@app.post("/Divide")
def divide_numbers(request: CalculationRequest):
    if request.num2 == 0:
        return {"error": "Division is not allowed by zero"}
    result = request.num1 / request.num2
    return { "result": result}

@app.post("/Sin")
def sin_function(request: CalculationRequest):
    radians = math.radians(request.num1)
    result = math.sin(radians)
    return { "resut": result}

@app.post("/Cos")
def cos_function(request: CalculationRequest):
    radians = math.radians(request.num1)
    result = math.cos(radians)
    return { "result": result}

@app.post("/Tan")
def tan_function(request: CalculationRequest):
    radians = math.radians(request.num1)  
    result = math.tan(radians)
    return { "result": result }

@app.post("/log")
def log_function(request: CalculationRequest):
    if request.num1 <= 0 or request.num2 <= 0:
        return { "error": "Logarithm of non-positive number(s) is not allowed" }
    result = math.log(request.num1, request.num2)
    return { "result": result }

@app.post("/ln")
def ln_function(request: CalculationRequest):
    if request.num1 <=0:
        return { "error": "Natural logarithm of a non-positive number(s) is not allowed"}
    result = math.log(request.num1)
    return { "result":result}

@app.post("/sqrt")
def square_root(request: CalculationRequest):
    if request.num1 < 0:
        return {"error": "Square root of a negative number(s) is not allowed"}
    result = math.sqrt(float(request.num1))
    return {"result": result}


@app.post("/factorial")
def factorial(request: CalculationRequest):
    if request.num1 < 0:
        return {"error": "Factorial of a negative number(s) is not allowed"}
    result = math.factorial(int(request.num1))
    return {"result": result}

@app.post("/pi")
def get_pi(request:CalculationRequest):
    result = math.pi * (request.num1)
    return {"result": result}

@app.post("/e")
def get_e(request: CalculationRequest):
    result = math.e * request.num1
    return {"result": result}