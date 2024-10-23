from typing import Union
from fastapi import FastAPI
import model_utils
from pydantic import BaseModel
app = FastAPI()

class HouseInput(BaseModel):
    size: float
    bedrooms: int
    garden: bool


model = model_utils.load_model("regression.joblib")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
def read_item(input: HouseInput):
    prediction = model.predict([[input.size, input.bedrooms, input.garden]])
    return {"prediction": prediction[0]}