from fastapi import FastAPI, Response

app = FastAPI()

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]


@app.get("/home")
def print_home():
    return {"message": "Hello World"}

@app.get("/")
def print_root():
    return {"message": "At root"}

@app.get("/products")
def product_index():
    return products

@app.get("/products/search")  # placing this below ("products/{id}") will have search requests send to that instead
def product_search(name, response: Response):
    found = [product for product in products if name.lower() in product["name"].lower()]

    if not found:
        response.status_code = 404
        return "No products found"

    return found if len(found) > 1 else found[0]

@app.get("/products/{id}")
def product(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            return product

    response.status_code = 404
    return "Not found"
