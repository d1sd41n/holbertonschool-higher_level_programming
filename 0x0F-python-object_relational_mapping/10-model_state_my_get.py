#!/usr/bin/python3
""" get first state
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
    get_states = session.query(State).filter_by(name=sys.argv[4]).first()
    if get_states:
        print("{}".format(get_states.id))
    else:
        print("Not found")
    session.close()
