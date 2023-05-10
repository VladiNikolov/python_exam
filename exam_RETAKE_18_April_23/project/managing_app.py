from project.route import Route
from project.user import User
from project.vehicles import base_vehicle
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPE = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_VEHICLE_TYPE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for rout in self.routes:
            if rout.start_point == start_point and rout.end_point == end_point and rout.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        for rout in self.routes:
            if rout.start_point == start_point and rout.end_point == end_point and rout.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

        id = len(self.routes) + 1

        rout = Route(start_point, end_point, length, id)
        self.routes.append(rout)

        for rout in self.routes:
            if rout.start_point == start_point and rout.end_point == end_point and rout.length > length:
                rout.is_locked = True

                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        for user in self.users:
            if user.is_blocked:
                return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        for rout in self.routes:
            if rout.is_locked:
                return f"Route {route_id} is locked! This trip is not allowed."


        #
        # if is_accident_happened:
        #     for vehicle in self.vehicles:
        #         vehicle.change_status()
        #         for user in self.users:
        #             user.decrease_rating()
        # user.increase_rating()
        #         for user in self.users:
        #             if user:
        #                 user.decrease_rating()
        #             else:
        #
        #                 return str(user)

    def repair_vehicles(self, count: int):
        pass

        # return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = f"*** E-Drive-Rent ***" + "\n"
        for user in self.users:
            result += str(user) + "\n"

        return result.strip()

