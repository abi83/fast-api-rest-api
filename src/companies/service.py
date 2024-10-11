from src.companies.repository import CompanyRepository, repository

class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.company_repository = repo

    async def get_companies(self, skip, limit):
        return await self.company_repository.get_companies(skip, limit)

    async def get_company(self, company_id: int):
        return await self.company_repository.get_company(company_id)

    def with_repository(self, repository: CompanyRepository):
        self.company_repository = repository

service = CompanyService(repository)