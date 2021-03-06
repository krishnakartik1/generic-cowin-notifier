from typing import Optional

from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

# from cowin_api import CoWinAPI
from dateutil import parser

from app.utils import *


app = FastAPI()
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

# cowin = CoWinAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.post("/login")
def postLogin(date: str = Form(...), pincode: str = Form(...)):
    dateCorrectFormat = parser.parse(date).strftime('%d-%m-%Y')
    try: 
        availableCenters = getavailabilitybypincode(pincode, dateCorrectFormat)
    except Exception as err:
        # print(err)
        # return err
        return str(err)
    return availableCenters
