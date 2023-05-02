from project.toy_store import ToyStore

from unittest import TestCase, main


class ToyStoreTest(TestCase):

    def test_correct_init(self):
        toy_store = ToyStore()
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)
        self.assertEqual(7, len(toy_store.toy_shelf))

    def test_add_toy_if_shelf_not_in_shelf_keys_raise(self):
        toy_store = ToyStore()
        toy_store.toy_shelf = {"A": "Bike",
            "B": "Truck"}
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy("C", "Doll")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_if_toy_exist_raise(self):
        toy_store = ToyStore()
        toy_store.toy_shelf = {"A": "Bike",
                               "B": "Truck"}
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy("A", "Bike")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_shelf_is_not_none_raise(self):
        toy_store = ToyStore()
        toy_store.toy_shelf = {"A": "Bike",
                               "B": "Truck",
                               "C": "Doll"}
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy("C", "Bear")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_successfully(self):
        toy_store = ToyStore()

        result = toy_store.add_toy("A", "Bike")
        self.assertEqual("Toy:Bike placed successfully!", result)
        self.assertEqual("Bike", toy_store.toy_shelf["A"])

    def test_remove_shelf_if_shelf_not_exist_raise(self):
        toy_store = ToyStore()
        toy_store.toy_shelf = {"A": "Bike",
                               "B": "Truck",
                               "C": "Doll"}

        with self.assertRaises(Exception) as ex:
            toy_store.remove_toy("D", "Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(3, len(toy_store.toy_shelf))

    def test_remove_toy_if_toy_in_that_shelf_not_exist_raise(self):
        toy_store = ToyStore()
        toy_store.toy_shelf = {"A": "Bike",
                               "B": "Truck",
                               "C": "Doll"}

        with self.assertRaises(Exception) as ex:
            toy_store.remove_toy("C", "Bear")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual("Doll", toy_store.toy_shelf["C"])

    def test_remove_toy_successfully(self):
        toy_store = ToyStore()
        toy_store.toy_shelf = {"A": "Bike"}

        result = toy_store.remove_toy("A", "Bike")
        self.assertEqual("Remove toy:Bike successfully!", result)
        self.assertIsNone(None, toy_store.toy_shelf["A"])



if __name__ == "__main__":
    main()