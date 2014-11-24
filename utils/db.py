# -*- coding: utf8 -*-

"""
    The ``db`` module
    ===================

    Contain all functions to access to DB.
"""

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

DB_FILE_PATH = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, 'db', 'ircbot.db'))
DB_ENGINE = sqlalchemy.create_engine(DB_FILE_PATH, echo=True)

from sqlalchemy.ext.declarative import declarative_base
DB_BASE = declarative_base()

from sqlalchemy.orm import sessionmaker
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def get_base():
    return DB_BASE


def get_session():
    return DB_SESSION
