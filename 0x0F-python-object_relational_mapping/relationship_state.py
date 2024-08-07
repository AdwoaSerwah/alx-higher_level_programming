#!/usr/bin/python3
"""Define the State class for SQLAlchemy."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class to represent the states table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )
