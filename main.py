# Code to demonstrate Synchronous REST Api - with the data stored in JSON file
# Demonstrated for GET, GET ID, POST, PUT AND DELETE HTTP Methods
# URL to run -> http://localhost:8001/docs which opens the Swagger API documentation
# Run Uvicorn - uvicorn main:app --reload --port=8001

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import service

app = FastAPI()

class Order(BaseModel):
    user_id: int
    product_price: int
    quantity: int
    

@app.get('/')
def getAllOrders():
    res = []
    data = service.get_all_order()
    for i in range(len(data)):
        res.append({'id':data[i][0], 'user_id':data[i][1], 'product_price':data[i][2], 'quantity':data[i][3], 'total_price':data[i][4]})
    return res


@app.get('/orders/{id}', status_code=200)
def get_order(id: int):
    try:
        data = service.get_order(id)
        return {'id':data[0], 'user_id':data[1], 'product_price':data[2], 'quantity':data[3], 'total_price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Failed to fetch order with id {id}")



@app.post('/orders', status_code=201)
def new_order(orderObj: Order):
    print(orderObj)
    try:
        new_order = {
            "user_id" : orderObj.user_id,
            "product_price" : orderObj.product_price,
            "total_price" : orderObj.product_price * orderObj.quantity,
            "quantity" : orderObj.quantity
        }
        data = service.create_order(new_order)

        return {'id':data[0], 'user_id':data[1], 'product_price':data[2], 'quantity':data[3], 'total_price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Order creation failed")


@app.delete('/orders/{id}',status_code=200)
def delete_order(id: int):
    try:
        data = service.delete_order(id);
        return data
    except:
        raise HTTPException(status_code=404, detail=f"There is no Order with id as {id}")

@app.put('/orders/{id}', status_code=200)
def change_order(id: int, orderObj: Order):
    try:
        new_order = {
            "user_id" : orderObj.user_id,
            "product_price" : orderObj.product_price,
            "total_price" : orderObj.product_price * orderObj.quantity,
            "quantity" : orderObj.quantity
        }
        data = service.update_order(id, new_order)
        return {'id':data[0], 'user_id':data[1], 'product_price':data[2], 'quantity':data[3], 'total_price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Order with id {id} does not exist")
