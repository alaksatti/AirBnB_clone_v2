#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              cascade="all")
    else:
        @property
        def cities(self):
            ''' returns the list of cities'''
            cities = models.storage.all(City)
            list_cities = []

            for city in cities:
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
