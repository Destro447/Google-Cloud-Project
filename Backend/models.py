from sqlalchemy import Column, String
from database import Base

class UserGreeting(Base):
    __tablename__ = "Greetings"

    Greeting = Column(String(200), index=True)
    
    
#to add another table

