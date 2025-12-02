from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the database engine
engine = create_engine("sqlite:///apartment_management.db")

# Base class for models
Base = declarative_base()

# Session factory
Session = sessionmaker(bind=engine)
session = Session()
