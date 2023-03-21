#!/usr/bin/python3
"""
Database storage
"""
from sqlalchemy import create_engine
import os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Object initialization"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine =
        create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}")

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            pass

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
