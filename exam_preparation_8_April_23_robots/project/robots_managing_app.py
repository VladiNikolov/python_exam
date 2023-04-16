from project.core.robot_factory import RobotFactory
from project.core.service_factory import ServiceFactory



class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

        self.service_factory = ServiceFactory()
        self.robot_factory = RobotFactory()

    def add_service(self, service_type: str, name: str):
        try:
            service = self.service_factory.create_service(service_type, name)
            self.services.append(service)
            return f"{service_type} is successfully added."
        except Exception as error:
            return str(error)

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        try:
            robot = self.robot_factory.create_robot(robot_type, name, kind, price)
            self.robots.append(robot)
            return f"{robot_type} is successfully added."
        except Exception as error:
            return str(error)

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        if robot.robot_type != service.__class__.__name__:
            return "Unsuitable service."

        if len(self.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        pass

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def __find_robot_by_name(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot
        return None

    def __find_service_by_name(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service
        return None

