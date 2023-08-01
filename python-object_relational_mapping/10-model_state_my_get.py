#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    # Create an instance of SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                            3306/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]))

    # Create a session to interact with the database
    session = Session(engine)
    # Query all State objects
    query = sys.argv[4]
    search_name = query
    try :
        states = session.query(State).filter(State.name == search_name).order_by(State.id).all()
        if len(states) == 0:
            print("Not Found")
        else:
            # Print the id and name of each State object
            for state in states:
                print(state.id)
    except: 
        print("oops")