import unittest
import carfactory
from mock import Mock

def constructorMock(name):
    """Create fake constructor that returns Mock object when invoked"""
    instance = Mock()
    instance._name_of_parent_class = name
    constructor = Mock(return_value=instance)
    return constructor

class CarFactoryTest(unittest.TestCase):

    def setUp():
        """Replace classes Wheel, Engine and Car with mock objects"""

        carfactory.Wheel = constructorMock("Wheel")
        carfactory.Engine = constructorMock("Engine")
        carfactory.Car = constructorMock("Car")

    def test_factory_creates_car():
        """Create car and check it has correct properties"""

        factory = carfactory.CarFactory()
        car_created = factory.create_car()

        # Check the wheels are created with correct radii
        carfactory.Wheel.assert_called_with(radius=50)
        carfactory.Wheel.assert_called_with(radius=50)
        carfactory.Wheel.assert_called_with(radius=60)
        carfactory.Wheel.assert_called_with(radius=60)

        # Check the engine is created with correct power
        carfactory.Engine.assert_called_once_with(power=500)

        # Check the car is created with correct engine and wheels
        wheel = carfactory.Wheel.return_value
        engine = carfactory.Engine.return_value
        carfactory.Car.assert_called_once_with(engine, [wheel, wheel, wheel, wheel])

        # Check the returned value is the car created
        self.assertEqual(car_created._name_of_parent_class, "Car")
