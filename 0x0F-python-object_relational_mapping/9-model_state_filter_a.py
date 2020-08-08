#!/usr/bin/python3
""" query the states from hbtn_0e_6_usa that starts with a
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
               sys.argv[1], sys.argv[2],
               'localhost', 3306, sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    get_states = session.query(State).filter(State.name.contains('a'))
    for state in get_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
