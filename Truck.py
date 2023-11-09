# This class shapes the data for Truck object
class Truck:
    def __init__(self, truck_id, mileage, truck_current_address, truck_current_time, truck_packages_list):
        self.truck_id = truck_id  # id of the truck
        self.mileage = mileage  # truck mileage
        self.truck_current_address = truck_current_address  # current address of the truck
        self.truck_current_time = truck_current_time  # current time of the truck
        self.truck_packages_list = truck_packages_list  # list of id of the packages loaded in the truck
