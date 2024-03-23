#!/usr/bin/python3
"""A unnitest for Place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """A unnitest for Place class """

    def __init__(self, *args, **kwargs):
        """A test for __init__ method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """A test fot city_id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ A test for User id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """A test for name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """A test for description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """A test fot numberd of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """A test fo rnumber of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ A test fot maximum guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ A test for price at night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """A test fot latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ A test fot longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """A test fot amenity id """
        place = Place()
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_instance(self):
        """A test place instance"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """A test for place attribute"""
        place = Place(name="Test Place", city_id="test_city_id", user_id="test_user_id")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.city_id, "test_city_id")
        self.assertEqual(place.user_id, "test_user_id")

    def test_place_relationship(self):
        """A test for place relationship"""
        place = Place()
        self.assertTrue(hasattr(place, 'reviews'))
        self.assertTrue(hasattr(place, 'amenities'))


if __name__ == '__main__':
    unittest.main()
