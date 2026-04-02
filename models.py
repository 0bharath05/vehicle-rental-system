class Vehicle:
    def __init__(self, vehicle_id, name, rent_per_km):
        self.vehicle_id = vehicle_id
        self.name = name
        self.rent_per_km = rent_per_km
        self.available = True


class Rental:
    def __init__(self, vehicle, user_name, id_proof):
        self.vehicle = vehicle
        self.user_name = user_name
        self.id_proof = id_proof
        self.start_time = None
        self.end_time = None
        self.km_travelled = 0
        self.cost = 0

    def calculate_cost(self):
        self.cost = self.km_travelled * self.vehicle.rent_per_km
        return self.cost