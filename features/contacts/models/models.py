from sqlalchemy import Column, ForeignKey, Integer, String
from app_config import Base


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    username = Column(String(500), nullable=False)
    email = Column(String(500), nullable=False)
    phone = Column(String(50), nullable=True)
    website = Column(String(500), nullable=True)

    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=True)

    def __repr__(self):
        return f'Contact: {self.name}, ({self.company.name})'

