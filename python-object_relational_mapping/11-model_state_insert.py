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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    
    print(new_state.id)
    
    session.close