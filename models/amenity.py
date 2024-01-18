#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity Class """

    if storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", backref="amenity")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes the basemodel class """
        super().__init__(*args, **kwargs)
