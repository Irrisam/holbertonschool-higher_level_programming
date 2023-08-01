#!/usr/bin/python3
"""class definition: City."""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
import sys

class City(Base):
    """City class used to work on a databse."""
    
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
