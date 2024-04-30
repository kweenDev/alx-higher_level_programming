#!/usr/bin/python3
# Defines a State model
# Inherits from SQLAlchemy Base and links to the MySQL table states.

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

"""
Represents a state for a MySQL database.
"""


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
