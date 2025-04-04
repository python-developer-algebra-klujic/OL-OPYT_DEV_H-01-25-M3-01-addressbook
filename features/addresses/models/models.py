from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from app_config import Base


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(length=500), nullable=True)
    suite = Column(String(length=250), nullable=True)
    city = Column(String(length=250), nullable=False)
    zip_code = Column(String(length=25), nullable=True)

    geo_id = Column(Integer, ForeignKey('geos.id'), nullable=True)

    contacts = relationship('Contact', backref=backref('address'))

    def __repr__(self):
        return f'Address: {self.city}, ({self.zip_code})'
