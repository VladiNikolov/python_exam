from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        robot_status = 'none' if len(self.robots) == 0 else ' '.join(r.name for r in self.robots)
        return f"{self.name} Main Service:\n" + f'Robots: {robot_status}'