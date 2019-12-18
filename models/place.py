#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             primary_key=True,
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             primary_key=True,
                             ForeignKey('amenities.id'),
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    name = Column(String(128),
                  nullable=False)

    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    description = Column(String(1024),
                         nullable=True)

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)

    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)

    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    latitude = Column(Float,
                      nullable=True)

    longitude = Column(Float,
                       nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               backref="place",
                               cascade="all")

        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            ''' returns list of review instances w/ place_id=curr place.id'''
            reviews = models.storage.all(Review)
            list_reviews = []
            for review in reviews:
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            ''' returns list of amenity instances based on attr amenity_ids '''
            list_amenity = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    list_amenity.append(amenity)
            return list_amenity

        @amenities.setter
        def amenities(self, obj):
            '''handles append for add an amenity.id to the attr amenity_ids'''
            if obj and isinstance(obj, Amenity):
                type(self).amenity_ids.append(obj.id)
