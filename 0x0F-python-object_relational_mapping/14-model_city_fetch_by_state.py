#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create an engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all cities with their state names
    results = (
            session.query(State.name, City.id, City.name)
            .join(City, State.id == City.state_id)
            .order_by(City.id)
            .all()
            )

    # Print results
    for st, c_id, c_name in results:
        print('{}: ({}) {}'.format(st, c_id, c_name))

    # Close the session
    session.close()
