#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.place import Place
from models.base_model import BaseModel, Base
from models import storage_type


class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        __tablename__: the name of the table created.
        id: primary key.
        email: the email address.
        password: User's password.
        first_name: user's first name.
        last_name: user's last name.
    """
    if storage_type == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self):
        """ Initializes the basemodel class """
        super().__init__(*args, **kwargs)
