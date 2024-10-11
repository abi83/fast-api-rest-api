from fastapi import APIRouter, Depends
from src.companies.service import CompanyService, service
from src.companies.schema import Company

router = APIRouter(prefix="/companies", tags=["companies"])

class CompanyController:
    def __init__(self, company_service: CompanyService = Depends()):
        self.company_service = company_service

    async def get_companies(self, skip, limit):
        return await self.company_service.get_companies(skip, limit)

    async def get_company_by_id(self, company_id: int):
        return await self.company_service.get_company(company_id)

controller = CompanyController(service)

@router.get("/", response_model=list[Company])
async def get_companies(skip: int = 0, limit: int = 100):
    return await controller.get_companies(skip, limit)

@router.get("/{company_id}", response_model=Company)
async def get_company_by_id(company_id: int):
    return await controller.get_company_by_id(company_id)
