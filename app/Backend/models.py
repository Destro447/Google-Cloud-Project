from sqlalchemy import Column, String,Integer
from Backend.database import Base

class UserGreeting(Base):
    __tablename__ = "greet"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Greetings = Column(String(200))
    
    
#to add another table

