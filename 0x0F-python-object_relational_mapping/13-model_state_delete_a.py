#!/usr/bin/python3
""" deletes states that contains a
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
    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
