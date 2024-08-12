#!/usr/bin/python3
"""Script that lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fake_relationship_state import State
# from relationship_city import City
from relationship_state import Base

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and their corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Display the results using the format method
    for state in states:
        print("{}: {}".format(state.id, state.name))
        # for city in state.cities:
            # print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
