from src.helper import *

from fastapi import FastAPI, form, Request, Response, FileUpload, File, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
import aiofiles
import json
import csv
from src.helper import llm_pipeline

app = FastAPI()
app.mounts("/static", StaticFiles(directory="static"), name = "static")

templates = Jinja2Templates(directory="templates")

