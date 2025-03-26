from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///databases/contact_manager.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
# Base.metadata.create_all(engine)
