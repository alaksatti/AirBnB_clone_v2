#!/usr/bin/python3                                                                                                
"""SQL DB Class"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
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
            classes = ['State', 'User', 'Place', 'City', 'Review', 'Amenity']
            for _class in classes:
                objs = self.__session.query(eval(_class))
                for obj in objs:
                    queried_results.append(obj)
                    
        for objects in queried_results:
            key = type(objects).__name__ + "." + str(objects.id)
            queried_dict[key] = objects
            
        return queried_dict

    def new(self, obj):
        """ adds object to current database session"""
        return self.__session.add(obj)


    def save(self):
        """ commit changes to current database session"""
        return self.__session.commit()


    def delete(self, obj=None):
        """ deletes from the current database session"""
        if obj:
            self.__session.delete(obj)


    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()


























