class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

# -----------------------------------------------------------------------


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_init_correctly_without_data(self):
        integer_list = IntegerList()
        self.assertEqual([], integer_list._IntegerList__data)

    def test_init_correctly_with_wrong_data(self):
        integer_list = IntegerList("asd", 5.6, 1.5)
        self.assertEqual([], integer_list._IntegerList__data)

    def test_init_correctly_with_integer_data(self):
        integer_list = IntegerList(5, 10, 20)
        self.assertEqual([5, 10, 20], integer_list._IntegerList__data)

    def test_get_data(self):
        integer_list = IntegerList(5, 10, 20)
        self.assertEqual([5, 10, 20], integer_list._IntegerList__data)

        result = integer_list.get_data()
        self.assertEqual([5, 10, 20], result)

    def test_add_method_incorrect_data_rises(self):
        integer_list = IntegerList(5, 10, 20)
        self.assertEqual([5, 10, 20], integer_list._IntegerList__data)

        with self.assertRaises(ValueError) as ve:
            integer_list.add("asd")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_correct_integer(self):
        integer_list = IntegerList(5, 10, 20)
        self.assertEqual([5, 10, 20], integer_list._IntegerList__data)

        integer_list.add(30)
        self.assertEqual([5, 10, 20, 30], integer_list._IntegerList__data)

    def test_index_remove_element(self):
        integer_list = IntegerList(5, 10, 20)
        integer_list.remove_index(0)

        self.assertEqual([10, 20], integer_list._IntegerList__data)

    def test_if_len_index_is_equal_to_index_rises(self):
        integer_list = IntegerList(5, 10, 20)
        self.assertEqual([5, 10, 20], integer_list._IntegerList__data)

        with self.assertRaises(IndexError) as ie:
            integer_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie:
            integer_list.remove_index(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_returns_element_at_the_removed_index(self):
        integer_list = IntegerList(5, 10, 20)
        result = integer_list.remove_index(2)
        self.assertEqual(20, result)

    def test_get_valid_index_return_element(self):
        integer_list = IntegerList(5, 10, 20)
        result = integer_list.get(0)
        self.assertEqual(5, result)

    def test_insert_invalid_index_rises(self):
        integer_list = IntegerList(5, 10, 20)

        with self.assertRaises(IndexError) as ie:
            integer_list.insert(5, 50)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_data_type_rises(self):
        integer_list = IntegerList(5, 10, 20)

        with self.assertRaises(ValueError) as ve:
            integer_list.insert(1, "asd")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_adds_element(self):
        integer_list = IntegerList(5, 10, 20)
        result = integer_list.insert(0, 3)
        self.assertEqual([3, 5, 10, 20], integer_list._IntegerList__data)

    def test_get_biggest(self):
        integer_list = IntegerList(5, 10, 20, -100, 100, 90)
        result = integer_list.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer_list = IntegerList(5, 10, 20, -100, 100, 90)
        result = integer_list.get_index(20)
        self.assertEqual(2, result)


if __name__ == '__main__':
    main()

