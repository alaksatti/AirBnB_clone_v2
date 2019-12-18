#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City",
                              cascade="all")


    
    else:
        name = ""
        @property
        def cities(self):
            ''' returns the list of cities'''
            cities = models.storage.all(models.City)
            list_cities = []

            for city in cities:
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
