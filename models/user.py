#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


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
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
