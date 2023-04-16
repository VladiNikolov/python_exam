from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 150)

    def test_init_correctly(self):
        vehicle = Vehicle(100, 150)

        self.assertEqual(1.25, vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(100, vehicle.fuel)
        self.assertEqual(100, vehicle.capacity)
        self.assertEqual(150, vehicle.horse_power)
        self.assertEqual(vehicle.fuel_consumption, vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_car_when_fuel_is_not_enough_rises(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_when_fuel_is_enough(self):
        distance = 10
        burned_fuel = distance * 1.25
        expected_result = self.vehicle.fuel - burned_fuel
        self.vehicle.drive(distance)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_if_fuel_more_then_capacity_rises(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_trunk_whit_enough_fuel(self):
        self.vehicle.fuel = 80
        self.vehicle.refuel(20)
        self.assertEqual(100, self.vehicle.fuel)


    def test_str_return_proper_string(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = str(self.vehicle)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()