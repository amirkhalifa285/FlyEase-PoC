from sqlalchemy import Column, Integer, String
from base import Base  # Import the shared Base


class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    gate = Column(String, nullable=False)


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


# Debugging to ensure tables are registered
print("Metadata tables in models.py:", Base.metadata.tables.keys())