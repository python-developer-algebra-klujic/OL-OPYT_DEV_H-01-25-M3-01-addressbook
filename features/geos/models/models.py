from sqlalchemy import Column, Integer, DECIMAL
from sqlalchemy.orm import relationship, backref
from app_config import Base


class Geo(Base):
    __tablename__ = 'geos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(DECIMAL(precision=10, scale=8), nullable=False)
    longitude = Column(DECIMAL(precision=10, scale=8), nullable=False)

    addresses = relationship('Address', backref=backref('geo'))

    def __repr__(self):
        return f'GEO: {self.latitude}, {self.longitude}'