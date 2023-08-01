#!/usr/bin/python3
"""Prints the State object with the name passed."""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    """Create an instance of SQLAlchemy engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))

    """Create a session to interact with the database and Query"""
    session = Session(engine)
    state_id = 2
    old_name = session.get(State, state_id)
    if old_name is None:
        print("Nothing")
    else:
        updated_name = "New Mexico"
        old_name.name = updated_name
        session.commit()
    session.close()