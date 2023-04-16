class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

# ----------------------------------------------------------------------------------------


from unittest import TestCase, main


class CarTest(TestCase):

    def test_car_init(self):
        car = Car("Audi", "A6", 8, 50)
        self.assertEqual("Audi", car.make)
        self.assertEqual("A6", car.model)
        self.assertEqual(8, car.fuel_consumption)
        self.assertEqual(50, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_return_correct_make(self):
        car = Car("Audi", "A6", 8, 50)
        self.assertEqual("Audi", car._Car__make)

    def test_return_make_raise(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_return_model_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_cannot_be_zero_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_cannot_be_negative_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_cannot_be_zero_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_cannot_be_negative_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_cannot_be_negative_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_negative_or_zero_refuel_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_whit_more_then_capacity(self):
        car = Car("Audi", "A6", 8, 50)

        car.refuel(car.fuel_capacity + 5)
        self.assertEqual(car.fuel_amount, car.fuel_capacity)

    def test_drive_more_then_possible_rises(self):
        car = Car("Audi", "A6", 8, 50)

        with self.assertRaises(Exception) as ex:
            car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()

