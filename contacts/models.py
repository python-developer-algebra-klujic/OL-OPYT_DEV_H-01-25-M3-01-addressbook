import json
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

class CompanyMapper:
    def from_json(self, company_json: str) -> Company:
        if isinstance(company_json, dict):
            return Company(
                name = company_json['name'],
                catch_phrase = company_json['catchPhrase'],
                best_sell = company_json['bs']
            )
        else:
            return None

    def to_json(self, company: Company) -> str:
        return json.dumps(company.__dict__)



class Geo(Base):
    __tablename__ = 'geos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(DECIMAL(precision=10, scale=8), nullable=False)
    longitude = Column(DECIMAL(precision=10, scale=8), nullable=False)

    addresses = relationship('Address', backref=backref('geo'))

    def __repr__(self):
        return f'GEO: {self.latitude}, {self.longitude}'

class GeoMapper:
    def from_json(self, geo_json: str) -> Geo:
        if isinstance(geo_json, dict):
            return Geo(
                latitude = geo_json['lat'],
                longitude = geo_json['lng']
            )
        else:
            return None

    def to_json(self, geo: Geo) -> str:
        return json.dumps(geo.__dict__)



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

class AddressMapper:
    def from_json(self, address_json: str) -> Address:
        if isinstance(address_json, dict):
            return Address(
                street = address_json['street'],
                suite = address_json['suite'],
                city = address_json['city'],
                zip_code = address_json['zipcode']
            )
        else:
            return None

    def to_json(self, address: Address) -> str:
        return json.dumps(address.__dict__)



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

class ContactMapper:
    def from_json(self, contact_json: str) -> Contact:
        if isinstance(contact_json, dict):
            return Contact(
                name = contact_json['name'],
                username = contact_json['username'],
                email = contact_json['email'],
                phone = contact_json['phone'],
                website = contact_json['website']
            )
        else:
            return None

    def to_json(self, contact: Contact) -> str:
        return json.dumps(contact.__dict__)
