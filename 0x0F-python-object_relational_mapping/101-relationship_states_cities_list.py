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

    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query all City objects
    cities = session.query(City).order_by(City.id).all()

    # Create a dictionary to hold State and its Cities
    states_dict = {}

    # Populate the dictionary with states and their cities
    for city in cities:
        state_id = city.state.id
        if state_id not in states_dict:
            states_dict[state_id] = {
                "state_name": city.state.name,
                "cities": []
            }
        states_dict[state_id]["cities"].append((city.id, city.name))

    # Sort the dictionary by state id
    sorted_states = sorted(states_dict.items())

    # Print results
    for state_id, state_info in sorted_states:
        print("{}: {}".format(state_id, state_info["state_name"]))
        for city_id, city_name in sorted(state_info["cities"]):
            print("\t{}: {}".format(city_id, city_name))

    # Close the session
    session.close()
