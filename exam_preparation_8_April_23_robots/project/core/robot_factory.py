from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot


class RobotFactory:
    robot_types = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def create_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.robot_types:
            raise Exception("Invalid robot type!")
        return self.robot_types[robot_type](name, kind, price)

