# Expected imports.

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from pandas import read_json


# imported my own data.
# from utils import database, network, time
import access


# To be sure that the customer send the data in teh correct format.
# I will need to add more styles.
class Input(BaseModel):
    # df_json: str
    cuantos: int


# Defining our API
app = FastAPI(title="Database Access",
              description="A simple api to connect with the tba_database that contain the predictions.",
              version="0.1")


@app.get('/last_predictions', tags=["LastPredictions"])
async def last_predictions(incoming_data: Input):
    df = access.get_cuantos(incoming_data.cuantos)
    return df.to_json()

