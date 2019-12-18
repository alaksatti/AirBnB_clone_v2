#!/usr/bin/python3
"""SQL DB Class"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from os import getenv


class DBStorage:
    """ DB Engine """

    __engine = None
    __session = None

    def __init__(self):
        """ initialize DB engine """
        db = getenv('HBNB_MYSQL_DB')
        usr = getenv('HBNB_MYSQL_USER')
        host = getenv('HBNB_MYSQL_HOST')
        pswd = getenv('HBNB_MYSQL_PWD')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(usr,
                                             pswd,
                                             host,
                                             db,
                                             pool_pre_ping=True))

        if getenv('HBNB_MYSQL_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query current database session"""
        queried_dict = {}
        if cls:
            queried_results = self.__session.query(cls).all()

        else:
            queried_results = []
            queried_results += self.__session.query(State).all()
            queried_results += self.__session.query(City).all()
            queried_results += self.__session.query(User).all()
            queried_results += self.__session.query(Place).all()

        for objects in queried_results:
            key = type(objects).__name__ + "." + str(objects.id)
            queried_dict[key] = objects

        return queried_dict

    def new(self, obj):
        """Adds object to current database session"""
        return self.__session.add(obj)

    def save(self):
        """Commits all changes the current database session"""
        return self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current DB session"""
        if obj:
            return self.__session.delete(obj)

    def reload(self):
        """Create all tables in the DB"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """Close the current session"""
        return self.__session.close()
