# Expected imports.

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from pandas import read_json, DataFrame
from io import StringIO


# imported my own data.
# from utils import database, network, time
import predictions
import access
# import access


# To be sure that the customer send the data in teh correct format.
# I will need to add more styles.
class Input(BaseModel):
    df_json: str


# Defining our API
app = FastAPI(title="Database Access",
              description="A simple api to connect with the tba_database that contain the predictions.",
              version="0.1")


@app.get('/get_predictions', tags=["Predictions"])
async def get_predictions(incoming_data: Input):
    df = read_json(StringIO(incoming_data.df_json))
    prediction = predictions.get_prediction(df)
    df['prediction'] = prediction
    access.load_predictions(df)
    return df.to_json()


@app.post('/train_model', tags=["Training"])
async def train_model(incoming_data: Input):
    df = read_json(StringIO(incoming_data.df_json))
    text = predictions.train_model(df)
    return text
