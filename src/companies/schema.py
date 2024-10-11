from pydantic import BaseModel

# todo: consider adding some inheritance
class Company(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class CompanyCreate(BaseModel):
    name: str

class CompanyUpdate(BaseModel):
    name: str
