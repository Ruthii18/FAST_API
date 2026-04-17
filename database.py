from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql+psycopg2://postgres:ruthii@localhost/ruthii_db"
engine=create_engine(db_url)
session=sessionmaker(autocommit=False, autoflush=False, bind=engine) 