#!/usr/bin/python3
"""This is to test City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class Test_City(test_basemodel):
    """ A Unnitest for city """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        city = City(name="Test City", state_id="test_state_id")
        self.assertEqual(city.name, "Test City")
        self.assertEqual(city.state_id, "test_state_id")

    def test_city_relationship(self):
        city = City()
        self.assertTrue(hasattr(city, 'places'))


if __name__ == '__main__':
    unittest.main()
