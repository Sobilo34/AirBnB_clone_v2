#!/usr/bin/python3
"""Defines the Place class."""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Table


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """A class for Place in a MySQL database"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        viewonly=False,
        back_populates="place_amenities"
    )

    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)
        self.amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """An object that gets a list of all linked Reviews."""
            return [review for review in self.reviews if review.place_id == self.id]

        @property
        def amenities(self):
            """The getter for linked Amenities."""
            return [amenity for amenity in self.amenities if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """The setter for linked Amenities."""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)

