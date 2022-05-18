from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DB = "sqlite:///py_library_fastapi.sql"

engine = create_engine(
    SQLALCHEMY_DB, connect_args={ "check_same_thread": False }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



