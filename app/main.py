
from sqlalchemy import Column, String,Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from fastapi import FastAPI,Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.declarative import declarative_base
import os

templates = Jinja2Templates(directory="templates")
app = FastAPI(templates=templates)


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
  return templates.TemplateResponse("templates/index.html", context=context)


class UserGreeting(Base):
    __tablename__ = "greet"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Greetings = Column(String(200))