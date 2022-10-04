from click import echo
from matplotlib.pyplot import connect
from regex import F
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# NOTE: ./blog.db is database name which was created on the same path.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# COMMENT: creating connection of database. By creating engine & Session.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread':False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# returns a new base class from which all mapped classes should inherit.
# When the class definition is completed, a new Table and mapper() will have been generated.
Base = declarative_base()







