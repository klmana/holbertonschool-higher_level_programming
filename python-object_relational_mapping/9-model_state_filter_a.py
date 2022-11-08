#!/usr/bin/python3
"""
  Lists all State objects that contain the letter a
  from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':

    # create engine, metadata for stored objects
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for data in session.query(State).order_by(
            State.id).filter(State.name.
                             like('%a%')):
        print("{}: {}".format(data.id, data.name))

    session.close()
