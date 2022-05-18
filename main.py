from fastapi import FastAPI, Path, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import sqlite3

API = FastAPI()


@API.get("/is_alive")
def is_alive():
    return {"status": True}
