#!usr/bin/python
"""a script that lists all State objects from the database"""
# Import the necessary modules
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
# Importing the Base and Stateclasses from model_state
if __name__ == "__main__":
    # Create a MySQL engine using SQLAlchemy
    # The script takes the MySQL username, password,
    # and database name as command-line arguments
    # and uses them to create the connection URL for the engine
    engine = create_engine(
         """mysql://{}:{}@localhost:3306/{}
         """.format(sys.argv[1], sys.argv[2], sys.argv[3])
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database and sort them by states.id
    # in ascending order
    states = session.query(State).order_by(State.id).all()

    # Print the results, displaying the state id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
