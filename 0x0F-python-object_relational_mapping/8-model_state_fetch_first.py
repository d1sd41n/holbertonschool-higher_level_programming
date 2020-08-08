#!/usr/bin/python3
"""query the first state from hbtn_0e_6_usa
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
    session = sessionmaker(engine)
    get_state = session().query(State).first()
    if get_state:
        print("{}: {}".format(get_state.id, get_state.name))
    else:
        print("Nothing")
    session().close()
