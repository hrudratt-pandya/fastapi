import imp
from fastapi import Body
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from database import Base

class Blog(Base):
    """ This class is table and __tablename__ is name of table.
        id, title, body are column name of the table.
        Integer, String are datatype


    Args:
        Base (_type_): Base is object avail in database.py
    """
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

class User(Base):
    """ This class is table and __tablename__ is name of table.
        id, title, body are column name of the table.
        Integer, String are datatype


    Args:
        Base (_type_): Base is object avail in database.py
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
