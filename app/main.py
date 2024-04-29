from fastapi import FastAPI,Request,HTTPException,Depends,status
from fastapi.templating import Jinja2Templates
from Backend.database import SessionLocal,engine
from sqlalchemy.orm import session
from pydantic import BaseModel
from typing import Annotated
from Backend import models
from Backend.models import UserGreeting


templates = Jinja2Templates(directory="templates")
app = FastAPI(templates=templates)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        # Fetch the first UserGreeting record and access only the 'Greetings' field
        greetings = db.query(UserGreeting).first()


        if greetings:
            greetings = greetings.Greetings  # Access the 'Greetings' field directly
        else:
            greetings = "Erreur retrieving data from database."

        yield db, greetings
    finally:
        db.close()



@app.get("/")
async def read_root(request: Request, db: session = Depends(get_db)):

  db, greetings = db
  context = {"request": request, "title": "Simple Page", "greeting": greetings}
  return templates.TemplateResponse("index.html", context=context)
