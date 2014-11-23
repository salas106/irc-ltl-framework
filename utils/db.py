import os

import sqlalchemy

db_file_path = os.path.abspath(os.path.join(os.sep, os.path.abspath(__file__), os.path.pardir, 'db', 'IrcBot.db'))
db_engine = sqlalchemy.create_engine(db_file_path, echo=True)

from sqlalchemy.ext.declarative import declarative_base
DbBase = declarative_base()

from sqlalchemy.orm import sessionmaker
DbSession = sessionmaker(bind=db_engine)


def get_base():
    return DbBase


def get_session():
    return DbSession