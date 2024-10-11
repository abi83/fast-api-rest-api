from time import sleep

from sqlalchemy.orm import Session
from sqlalchemy import text, Engine

from src.companies.schema import Company
from src.database.connection import session, connection
from src.companies.models import CompanyTable

class CompanyRepository:
    def __init__(self, s: Session, c: Engine):
        self.__connection = c
        self.__session = s

    # todo: this can be moved to a parent class (or mixin)
    @property
    def database(self):
        try:
            self.__session.scalar(text('SELECT 1'))
            return self.__session
        except Exception as exception:
            print('Database connection is lost: ', exception)
            attempts = 0
            while attempts < 3:
                sleep(1)
                print('Trying to reconnect. Attempt: ', attempts)
                try:
                    self.__connection.connect()
                    self.__session.rollback()
                    return self.__session
                except Exception as e:
                    attempts += 1
                    print('Error while reconnecting to DB: ', e)
            raise Exception('Database connection fully lost')

    async def get_companies(self, skip: int = 0, limit: int = 100):
        orm_companies =  self.database.query(CompanyTable).offset(skip).limit(limit).all()
        return [Company.model_validate(company) for company in orm_companies]

    async def get_company(self, company_id: int):
        orm_company = self.database.query(CompanyTable).get(company_id)
        return Company.model_validate(orm_company)

repository = CompanyRepository(session, connection)
