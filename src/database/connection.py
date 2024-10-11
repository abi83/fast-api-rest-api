from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:123@localhost:5432/fast"

connection: Engine = create_engine(DATABASE_URL)
session_fabric = sessionmaker(autocommit=False, autoflush=False, bind=connection)
session = session_fabric()

Base = declarative_base()