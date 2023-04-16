from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("TestName", 3)

    def test_correct_init(self):
        train = Train("Express", 100)
        self.assertEqual("Express", train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual([], train.passengers)
        # self.assertEqual("Train is full", Train.TRAIN_FULL)
        # self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        # self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        # self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        # self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        # self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_passenger_if_train_is_full_raise(self):
        self.train.passengers = ["Pesho", "Gosho", "Vladi"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Desi")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_adds_passenger_if_exist_raise(self):
        self.train.passengers = ["Pesho", "Gosho"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Gosho")
        self.assertEqual("Passenger Gosho Exists", str(ve.exception))


    def test_add_adds_passengers_and_return_str(self):
        passenger_name = "Vladi"
        result = self.train.add(passenger_name)

        self.assertEqual(f"Added passenger {passenger_name}", result)
        self.assertTrue(passenger_name in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_remove_passenger_if_not_exist_raise(self):
        self.train.passengers = ["Pesho", "Gosho", "Vladi"]

        with self.assertRaises(ValueError) as ve:
            self.train.remove("Desi")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_passenger_return_proper_str(self):
        self.train.passengers = ["Pesho", "Gosho", "Vladi"]
        result = self.train.remove("Vladi")
        self.assertEqual("Removed Vladi", result)





if __name__ == "__main__":
    main()