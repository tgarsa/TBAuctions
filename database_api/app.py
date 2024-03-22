# Expected imports.

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from pandas import read_json


# imported my own data.
# from utils import database, network, time
import access

# To add security
import security as sec
from datetime import timedelta
from typing_extensions import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm



# To be sure that the customer send the data in teh correct format.
# I will need to add more styles.
class Input(BaseModel):
    # df_json: str
    cuantos: int


# Defining our API
app = FastAPI(title="Database Access",
              description="A simple api to connect with the tba_database that contain the predictions.",
              version="0.1")

@app.post("/token", response_model=sec.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = sec.authenticate_user(sec.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=sec.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = sec.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get('/last_predictions', tags=["LastPredictions"])
async def last_predictions(incoming_data: Input,
                          current_user: Annotated[sec.User, Depends(sec.get_current_active_user)]
                          ):
    df = access.get_cuantos(incoming_data.cuantos)
    return df.to_json()

