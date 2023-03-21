#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """User class, inherits from BaseModel & Base"""
        __tablename__ = 'users'
        email = Column(String(128),
                       nullable=False)
        password = Column('password',
                           String(128),
                           nullable=False)
        first_name = Column(String(128),
                            nullable=True)
        last_name = Column(String(128),
                           nullable=True)
