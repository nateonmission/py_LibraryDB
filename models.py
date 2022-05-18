from sqlalchemy import Column, Integer, String
from db import Base


class Publisher:
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(Author)
    publisher = Column(Publisher)
    ISBN = Column(String)
    ISBN13 = Column(String)
