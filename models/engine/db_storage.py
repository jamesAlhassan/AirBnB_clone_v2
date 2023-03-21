#!/usr/bin/python3
"""
Database storage
"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Object initialization"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{password}@{host}/{db}")

    if getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all on the current database"""
        if cls is not None:
            results = self.__session.query(cls).all()
        else:

            results = self.__session.query(City).all()
            results += self.__session.query(State).all()

        results_dict = {}
        for result in results:
            results_dict[f"{type(result).__name__}.{result.id}"] = result
            return results_dict

    def new(self, obj):
        """Adds a new object"""
        self.__session.add(obj)

    def save(self):
        """saves  current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object"""
        if obj:
            return
        else:
            self.__session.delete(obj)

    def reload(self):
        """create all tables of dtabase"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
