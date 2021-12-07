from fastapi import FastAPI, Response

app = FastAPI()

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]

@app.get("/products")
def product_index():
    return products
    # return {"message": "Dank"}

@app.get("/products/{id}")
def product(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            return product

    response.status_code = 404
    return "Not found"

@app.get("/home")
def print_home():
    return {"message": "Hello World"}

@app.get("/")
def print_root():
    return {"message": "At root"}
