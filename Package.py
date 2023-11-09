# This class shapes the data for the package object, which will later be inserted in the hash table
class Package:
    def __init__(self, package_id, delivery_address, address_id, delivery_city, delivery_state, delivery_zip, deadline,
                 weight,
                 delivery_notes, delivery_status, delivery_time, package_truck_id, departure_time):
        self.package_id = package_id  # id of the package
        self.delivery_address = delivery_address  # address where the package needs to be delivered
        self.address_id = address_id  # id of the address of the package
        self.delivery_city = delivery_city  # city of the delivery address
        self.delivery_state = delivery_state  # state of the delivery address
        self.delivery_zip = delivery_zip  # zip code of the delivery address
        self.deadline = deadline  # the package delivery deadline
        self.weight = weight  # the package weight in pounds
        self.delivery_notes = delivery_notes  # package delivery notes
        self.delivery_status = delivery_status  # package delivery status
        self.delivery_time = delivery_time  # time at which the package is delivered
        self.package_truck_id = package_truck_id  # id of the truck that delivers the package
        self.departure_time = departure_time  # time at which the package leaves the hub
