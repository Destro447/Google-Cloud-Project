from fastapi import FastAPI,Request,HTTPException,Depends,status
from fastapi.templating import Jinja2Templates
from Backend.database import SessionLocal,engine
from sqlalchemy.orm import session
from pydantic import BaseModel
from typing import Annotated
import Backend.models 


templates = Jinja2Templates(directory="templates")
app = FastAPI(templates=templates)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root(request: Request):
    # Pass context data to the template for dynamic rendering
    context = {"request": request, "title": "Simple Page"}
    return templates.TemplateResponse("index.html", context=context)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

