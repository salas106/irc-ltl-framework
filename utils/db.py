import os

import sqlalchemy

db_file_path = os.path.abspath(os.path.join(os.sep, os.path.pardir(os.path.dirname(__file__)), 'db', 'IrcBot.db'))
sqlalchemy.create_engine(db_file_path, echo=True)
