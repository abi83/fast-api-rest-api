from contextlib import asynccontextmanager

from src.database.connection import connection, session, Base
from fastapi import FastAPI

from src.companies.controller import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        connection.connect()
    except Exception as e:
        print('Database connection failed', e)
    yield
    session.close_all()

# todo: use a separate script for creating tables or migrations
# Base.metadata.create_all(bind=connection)

app = FastAPI(
    title="Services List",
    lifespan=lifespan,
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return "Company API"