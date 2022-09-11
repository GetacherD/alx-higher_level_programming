#!/usr/bin/python3
"""
First Sqlalchemy ORM
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import City


Base = declarative_base()


class State(Base):

    """ State ORM Model """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128))
    cities = relationship("City", backref="states", cascade="all, delete")

    def __repr__(self):
        return self.id + "::" + self.name
