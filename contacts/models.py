from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
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


class Geo(Base):
    __tablename__ = 'geos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(DECIMAL(precision=10, scale=8), nullable=False)
    longitude = Column(DECIMAL(precision=10, scale=8), nullable=False)

    addresses = relationship('Address', backref=backref('geo'))

    def __repr__(self):
        return f'GEO: {self.latitude}, {self.longitude}'


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(length=500), nullable=True)
    suite = Column(String(length=250), nullable=True)
    city = Column(String(length=250), nullable=False)
    zip_code = Column(String(length=25), nullable=True)


    geo_id = relationship(Geo, ForeignKey('geos.id'))
    contacts = relationship('Contact', backref=backref('address'))
    # TODO dodati __repr__ metodu


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    username = Column(String(500), nullable=False)
    email = Column(String(500), nullable=False)
    phone = Column(String(50), nullable=True)
    website = Column(String(500), nullable=True)

    address_id = relationship(Address, ForeignKey('addresses.id'))
    company_id = relationship(Company, ForeignKey('companies.id'))

    # TODO dodati __repr__ metodu
