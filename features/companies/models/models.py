from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from app_config import Base


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=250), nullable=False)
    catch_phrase = Column(String(1000), nullable=False)
    best_sell = Column(String(1000), nullable=False)

    contacts = relationship('Contact', backref=backref('company'))

    def __repr__(self):
        return f'Company {self.name}'
