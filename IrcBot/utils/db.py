import os
import os.path as path

import sqlalchemy

db_file_path = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, path.pardir, 'db', 'IrcBot.db'))
db_engine = sqlalchemy.create_engine(db_file_path, echo=True)

from sqlalchemy.ext.declarative import declarative_base
DbBase = declarative_base()

from sqlalchemy.orm import sessionmaker
DbSession = sessionmaker(bind=db_engine)


def get_base():
    return DbBase


def get_session():
    return DbSession