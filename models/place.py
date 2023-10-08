#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Float, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref='place')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False, back_populates="place_amenities")

    @property
    def reviews(self):
        """getter attribute reviews that returns the list
        of Review instances with place_id"""
        from models import storage
        dict1 = storage.all('Review')
        list1 = []
        for v in dict1.values():
            if v.place_id == self.id:
                list1.append(v)
        return list1

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def gamenities(self):
            """getter attribute reviews that returns the list
            of Review instances with place_id"""
            from models import storage
            dict1 = storage.all('Amenity')
            list1 = []
            for v in dict1.values():
                if v.id in self.amenity_ids:
                    list1.append(v)
            return list1

        @gamenities.setter
        def gamenities(self, obj):
            """Setter attribute amenities that handles append
            method for adding an Amenity.id"""
            if type(obj).__name__ == "Amenity":
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
