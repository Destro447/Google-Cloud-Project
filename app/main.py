from fastapi import FastAPI,Request,HTTPException,Depends,status
from fastapi.templating import Jinja2Templates
from Backend.database import SessionLocal,engine
from sqlalchemy.orm import session
from pydantic import BaseModel
from typing import Annotated
import Backend.models as models
from Backend.models import UserGreeting


templates = Jinja2Templates(directory="templates")
app = FastAPI(templates=templates)

models.Base.metadata.create_all(bind=engine)

"""@app.get("/")
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
"""


def get_db():
  db = SessionLocal()
  try:
    greeting = db.query(UserGreeting).first()  
    if not greeting:
      greeting = "Erreur retrieving data from database."
    yield db, greeting 
  finally:
    db.close()


@app.get("/")
async def read_root(request: Request, db: session = Depends(get_db)):

  db, greeting = db
  context = {"request": request, "title": "Simple Page", "greeting": greeting.Greeting}
  return templates.TemplateResponse("index.html", context=context)
