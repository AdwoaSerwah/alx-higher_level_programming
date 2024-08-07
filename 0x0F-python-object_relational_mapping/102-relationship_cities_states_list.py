#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their related states, ordered by city id
    results = (
        session.query(City)
        .join(State)
        .order_by(City.id)
        .all()
    )

    # Print results
    for city in results:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
