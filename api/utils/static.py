from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

def static_files(app: FastAPI):
    """Setup static file handling for the FastAPI application"""
    app.mount("/static", StaticFiles(directory="static"), name="static")
