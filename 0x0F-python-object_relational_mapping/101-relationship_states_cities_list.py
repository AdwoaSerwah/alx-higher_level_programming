#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database
hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create engine and bind it to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    states_1 = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states_1:
        print("{}: {}".format(state.id, state.name))
        for city_1 in state.cities:
            print("\t{}: {}".format(city_1.id, city_1.name))

    # Close the session
    session.close()
