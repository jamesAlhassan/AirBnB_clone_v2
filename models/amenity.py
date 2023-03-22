#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import type_storage


class Amenity(BaseModel, Base):
    """Representation of Amenity Class"""
    __tablename__ = 'amenities'

    if type_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
