from project.robot import Robot

from unittest import TestCase, main

class RobotTest(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("ID5", "Military", 10, 50)

    def test_correct_init(self):
        robot = Robot("ID5", "Military", 10, 50)

        self.assertEqual("ID5", robot.robot_id)
        self.assertEqual("Military", robot.category)
        self.assertEqual(10, robot.available_capacity)
        self.assertEqual(50, robot.price)
        self.assertEqual([], robot.hardware_upgrades)
        self.assertEqual([], robot.software_updates)

    def test_setter_if_category_not_in_category_list_raise(self):
        ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
        with self.assertRaises(ValueError) as ve:
            robot = Robot("ID5", "Mil", 10, 50)
        self.assertEqual(f"Category should be one of '{ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_setter_if_price_is_negative_raises(self):
        with self.assertRaises(ValueError) as ve:
            robot = Robot("ID5", "Military", 10, -1)
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_if_hardware_component_add(self):
        robot = Robot("ID5", "Military", 10, 50)
        robot.hardware_upgrades = ["RAM", "VideoCard", "Processor","ROM"]

        result = self.robot.upgrade("ROM", 5)
        self.assertEqual('Robot ID5 was upgraded with ROM.', result)

    def test_upgrade_if_hardware_component_exist(self):
        robot = Robot("ID5", "Military", 10, 50)
        robot.hardware_upgrades = ["RAM", "VideoCard", "Processor"]

        result = robot.upgrade("RAM", 5)
        self.assertEqual("Robot ID5 was not upgraded.", result)

    def test_update_not_updated(self):
        robot = Robot("ID5", "Military", 10, 50)
        robot.software_updates = [2, 3, 4]

        result = robot.update(1, 10)
        self.assertEqual(f"Robot ID5 was not updated.", result)

    def test_update_succesfull(self):
        robot = Robot("ID5", "Military", 10, 50)
        robot.software_updates = [2, 3, 4]

        result = robot.update(5, 10)
        self.assertEqual(f'Robot ID5 was updated to version 5.', result)

    def test_gt_compares_price_is_greater_other_price(self):
        robot = Robot("ID5", "Military", 10, 60)
        other_robot = Robot("ID6", "Education", 15, 50)

        self.assertEqual(True, robot.price > other_robot.price)
        self.assertEqual(f'Robot with ID ID5 is more expensive than Robot with ID ID6.', robot.__gt__(other_robot))

    def test_gt_compares_price_is_equal_other_price(self):
        robot = Robot("ID5", "Military", 10, 50)
        other_robot = Robot("ID6", "Education", 15, 50)

        self.assertEqual(True, robot.price == other_robot.price)
        self.assertEqual(f'Robot with ID ID5 costs equal to Robot with ID ID6.', robot.__gt__(other_robot))

    def test_gt_compares_price_is_cheaper_then_other_price(self):
        robot = Robot("ID5", "Military", 10, 50)
        other_robot = Robot("ID6", "Education", 15, 60)

        self.assertEqual(True, robot.price < other_robot.price)
        self.assertEqual(f'Robot with ID ID5 is cheaper than Robot with ID ID6.', robot.__gt__(other_robot))





if __name__ == "__main__":
    main()
