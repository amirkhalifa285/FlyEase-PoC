import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import platform
from base import Base  # Import the shared Base

if platform.system() == "Windows":
    os.add_dll_directory(r"C:\Program Files\PostgreSQL\17\bin")

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    """
    This import is necessary to register all models with the Base metadata.
    Do not remove this import.
    """
    import models  # noqa: F401

    # Debugging Metadata
    print("Registered tables in metadata before create_all:", Base.metadata.tables.keys())

    # Drop and recreate tables
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

    # Verify tables in the database
    from sqlalchemy import inspect

    inspector = inspect(engine)
    print("Existing tables in database:", inspector.get_table_names())
