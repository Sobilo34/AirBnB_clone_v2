#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import sqlalchemy
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    type_of_storage = getenv("HBNB_TYPE_STORAGE")
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if type_of_storage != 'db':
        @property
        def cities(self):
            """
            Returns the list of City instances with equal state_id
            """
            cities = models.storage.all(City)
            self.__cities = [
                city for city in cities.values()
                if city.state_id == self.id
            ]
            return self.__cities
