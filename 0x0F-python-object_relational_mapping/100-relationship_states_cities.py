#!/usr/bin/python3
"""Creates a State and a City in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create an engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add to session and commit
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Close the session
    session.close()
