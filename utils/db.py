# -*- coding: utf8 -*-

__author__ = 'Salas'
__copyright__ = 'Copyright 2014 LTL'
__credits__ = ['Salas']
__license__ = 'MIT'
__version__ = '0.2.0'
__maintainer__ = 'Salas'
__email__ = 'Salas.106.212@gmail.com'
__status__ = 'Pre-Alpha'

import os
import os.path as path

import sqlalchemy

db_file_path = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, 'db', 'ircbot.db'))
db_engine = sqlalchemy.create_engine(db_file_path, echo=True)

from sqlalchemy.ext.declarative import declarative_base
DbBase = declarative_base()

from sqlalchemy.orm import sessionmaker
DbSession = sessionmaker(bind=db_engine)


def get_base():
    return DbBase


def get_session():
    return DbSession
