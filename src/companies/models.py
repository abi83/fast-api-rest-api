from sqlalchemy import Column, Integer, String

from src.database.connection import Base

class CompanyTable(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
