from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class ServiceFactory:
    service_types = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    def create_service(self, service_type: str, name: str):
        if service_type not in self.service_types:
            raise Exception("Invalid service type!")

        return self.service_types[service_type](name)