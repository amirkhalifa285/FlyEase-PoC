from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    gate = Column(String, nullable=False)
