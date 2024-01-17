#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.city import City

class State(BaseModel, Base):
    """ State class """

    if storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self):
        """ Initializes the basemodel class """
        super().__init__(*args, **kwargs)

    if storage_type != "db":
        @property
        def cities(self):
            """ Returns the list of cities in the filestorage """
            all_city = storage.all(City)
            all_city_match = []
            for city in all_city:
                if city.state_id == self.id:
                    all_city_match.append(city)
            return all_city_match
