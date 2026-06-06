from fastapi import FastAPI
from dotenv import load_dotenv
from routes.base import base_router
import os

load_dotenv()

app = FastAPI()

app.include_router(base_router)
