#!/usr/bin/python3
"""
Database storage
"""

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Object initialization"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine == create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}")
