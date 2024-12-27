from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Define the database URL with asyncpg
DATABASE_URL = os.getenv("DATABASE_URL")  # Example: postgresql+asyncpg://user:password@localhost/dbname

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create an async engine and session factory
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency for database sessions
async def get_db():
    async with SessionLocal() as session:
        yield session
