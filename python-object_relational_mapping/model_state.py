#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base():"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """instance for the states table"""
    __tablename__ = "states"
    """ primary key gives unique attributes non null and autogened"""
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
