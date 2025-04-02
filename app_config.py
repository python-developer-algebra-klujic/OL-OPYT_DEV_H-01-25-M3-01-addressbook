from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class AppConfig:
    def __init__(self):
        self.engine = create_engine('sqlite:///databases/address_book.db')
        self.session = None
        self.base = None

        self.init_data()

    def init_data(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.base = declarative_base()

        self.base.metadata.create_all(self.engine)
