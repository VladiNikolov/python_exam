from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 180.00)

    def drive(self, mileage: float):
        result = (mileage / 180.00) * 100
        result = round(result)
        self.battery_level -= result + 5

