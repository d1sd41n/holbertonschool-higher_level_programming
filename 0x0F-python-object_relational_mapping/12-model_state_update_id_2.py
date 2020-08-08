#!/usr/bin/python3
""" changes the name of a state that has a id=2
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
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
