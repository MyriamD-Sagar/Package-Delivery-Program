# Myriam Drouin-Sagar, student ID: 007857813
import datetime

import Truck

from utils import LoadData, DistanceUtil, TimeUtil

# instantiation of truck objects by manually loading the trucks
truck1 = Truck.Truck(1, 0.0, '4001 South 700 East', datetime.timedelta(hours=8), [16, 15, 20, 21, 14, 19, 13, 34, 39,
                                                                                  22, 40, 4, 1, 29, 30, 37])
truck2 = Truck.Truck(2, 0.0, '4001 South 700 East', datetime.timedelta(hours=10, minutes=20), [5, 38, 9, 8, 3, 36, 18,
                                                                                               7, 12, 23])
truck3 = Truck.Truck(3, 0.0, '4001 South 700 East', datetime.timedelta(hours=9, minutes=5), [6, 25, 26, 31, 32, 17, 33,
                                                                                             2, 28, 27, 35, 11, 24, 10])

# gets the hash table by calling the load_package() method
hash_table = LoadData.load_package('csvFiles/packages.csv')


# This method updates package objects according to which truck they were loaded in.
# Then, it inserts the new items (packages) in the hash table.
# It receives a truck object, which attributes will be used to update the package's attributes.
# Run-time complexity: O(n^2)
def update_package(truck):
    package_list = truck.truck_packages_list  # list of package's id in the truck
    # searches through the hash table with each package's id found in the list
    for id in package_list:
        package = hash_table.get_item(id)  # run-time complexity of O(n)

        # updates the package truck id
        package.package_truck_id = truck.truck_id

        # the package departure time from hub is set to the truck initial departure time
        package.departure_time = truck.truck_current_time

        # finds the address id for each package's delivery address and assign it to package's address id
        package.address_id = DistanceUtil.find_address_index(package.delivery_address)  # run-time complexity of O(1)

        # inserts the updated item (package) in the hash table
        hash_table.insert_item(id, package)  # run-time complexity of O(n)


# updates and inserts package's object in hash table by calling update_package() with truck object as argument
update_package(truck1)
update_package(truck2)
update_package(truck3)


# This method delivers all packages by receiving a truck object (parameter).
# It loops the method call find_closest_address() to get the closest address from the list of package id the truck.
# It finds the index of the closest address and
# loops through the list of id to search in hash table for the package(s) that has the same address index.
# Then, the package(s) found becomes the next package to be delivered
# The id of the next package is removed from the list of package id in the truck.
# Run-time complexity: O(n^3)
def package_delivery(truck):
    package_list = truck.truck_packages_list  # list of package's id in the truck
    current_address = truck.truck_current_address  # current address initial value is the truck initial address

    # loops through the list of package's id in the truck and continuously finds the next closest address
    # loops until there is no more package id in the truck's package list
    while len(package_list) > 0:
        # finds the closest address from the truck current address
        next_package_address = DistanceUtil.find_closest_address(current_address, package_list)  # run-time completity of O(n)

        # finds the index of the closest address
        address_index = DistanceUtil.find_address_index(next_package_address)  # run-time complexity of O(n)

        # finds the distance from current address to the closest address
        distance = DistanceUtil.find_distance(current_address, next_package_address)  # run-time complexity of O(n)

        # searches in hash table to find the package associated with the address index of the closest address
        for id in package_list:
            package = hash_table.get_item(id)  # run-time complexity of O(1)

            # if the package address id is equal to the index of the closest address, the package is delivered
            if package.address_id == address_index:
                next_package = package

                truck.truck_current_address = next_package.delivery_address  # updates the truck current address
                truck.mileage += distance  # updates the truck mileage with the distance
                truck.truck_current_time += datetime.timedelta(hours=distance / 18.0)  # updates the truck current time

                next_package.delivery_time = truck.truck_current_time  # updates the package delivery time

                hash_table.insert_item(id, next_package)  # inserts the updated package in hash table O(n)

                package_list.remove(id)  # removes the package id from the list of package in the truck

                current_address = next_package_address  # updates the current address with the package address

    # truck number 1 needs to come back to the hub when all its packages are delivered
    if truck.truck_id == 1:
        # finds the distance from current address to the hub
        distance = DistanceUtil.find_distance(truck.truck_current_address, '4001 South 700 East')

        truck.mileage += distance  # updates truck1 final mileage with the distance
        truck.truck_current_time += datetime.timedelta(hours=distance / 18.0)  # updates truck1 final time
        truck.truck_current_address = '4001 South 700 East'  # updates truck1 final address with the address of the hub


# delivers the packages in each truck by calling the method package_delivery() with truck object as argument
package_delivery(truck1)
package_delivery(truck2)
package_delivery(truck3)


# This class is the user interface.
# It allows the user to view package(s) delivery status and information at a time chosen by the user
class Main:
    try:
        print("Welcome to the Western Governors University Parcel Service (WGUPS)\n")
        print("The total mileage for the route is " + str(truck1.mileage + truck2.mileage + truck3.mileage))
        input_time = input("Please enter the desired time (format --> hh:mm:ss) to verify package(s) delivery status and information: ")

        # calls the method string_to_datetime to convert the string input into a datetime(timedelta) type
        input_time_delta = TimeUtil.string_to_datetime(input_time)

        # loops through all packages id by calling the method get_item() and passing each id as the key argument
        # run-time complexity of this portion of code is O(n^2)
        for id in range(1, 41):
            p = hash_table.get_item(id)

            # updates delivery status by calling verify_time() method and inserts updated package in hash table
            p.delivery_status = TimeUtil.verify_time(p.departure_time, p.delivery_time, input_time_delta)
            hash_table.insert_item(id, p)  # run-time complexity of O(n)

        print("~~~~~~~~~~~~~~~~~~~  Menu Options  ~~~~~~~~~~~~~~~~~~~")
        print("1. Print all packages delivery status and information\n")
        print("2. Print a single package delivery status and information\n")
        print("3. Exit the program\n")

        # gets the user input choice option as an integer
        input_choice = int(input("Please enter the number associated with the information you would like to display: "))

        # if user chooses option 1, all packages information will be displayed according to the user input time
        if input_choice == 1:
            print("\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ALL PACKAGES INFORMATION AT " +
                  str(input_time_delta) + "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ")

            # loops through all the package object in the hash table to get the package objects
            # Run-time complexity of this segment O(n^2)
            for p_id in range(1, 41):
                p = hash_table.get_item(p_id)  # O(n)

                # formats the output of package delivery status (updated above according to the user input time)
                if p.delivery_status == "Delivered":
                    p.delivery_status = p.delivery_status + " by Truck-" + str(p.package_truck_id) + " at " + str(
                        p.delivery_time)
                if p.delivery_status == "En Route":
                    p.delivery_status = p.delivery_status + " in Truck-" + str(p.package_truck_id) + " since " + str(
                        p.departure_time)

                # prints one by one each package objects information
                print(
                    "Package ID: {} | Address: {} | State: {} | City: {} | Zip: {} | Weight: {} | Deadline: {} | Delivery Status: {}"
                    .format(str(p.package_id), p.delivery_address, p.delivery_state, p.delivery_city, p.delivery_zip,
                            p.weight, p.deadline, str(p.delivery_status)))

        # if user chooses option 2, a single package information is displayed according to the user input time
        elif input_choice == 2:
            # gets the user input (package id) as an integer
            input_id = int(input("Please enter the id of the package: "))

            # gets the package object (item) associated with the id (key)
            package_obj = hash_table.get_item(input_id)  # run-time complexity of O(n)

            # if the package id cannot be found in hash table, the program closes
            if package_obj is None:
                print("\n~~ Invalid Package ID ~~")
                print("   Closing WGUPS")
                exit()
            # else, the package object is loaded
            p = package_obj

            # formats the output the package delivery status (previously updated according to the user input time)
            # if the package is delivered, the delivery status outputs the truck that carried the package and
            # the time at which the package was delivered
            if p.delivery_status == "Delivered":
                p.delivery_status = p.delivery_status + " by Truck-" + str(p.package_truck_id) + " at " + \
                                    str(p.delivery_time)
            # if the package as left the hub, the delivery status outputs the truck carrying the package and
            # the time at which the package left.
            if p.delivery_status == "En Route":
                p.delivery_status = p.delivery_status + " in Truck-" + str(p.package_truck_id) + " since " + \
                                    str(p.departure_time)

            print("\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  INFORMATION OF PACKAGE (" + str(
                input_id) + ") AT " +
                  str(input_time_delta) + "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ")

            # prints the package information
            print(
                "Package ID: {} | Address: {} | State: {} | City: {} | Zip: {} | Weight: {} | Deadline: {} | Delivery Status: {}"
                .format(str(p.package_id), p.delivery_address, p.delivery_state, p.delivery_city, p.delivery_zip,
                        p.weight, p.deadline, str(p.delivery_status)))

        # if the user chooses option 3, the program closes
        elif input_choice == 3:
            print("\n~~ Closing WGUPS ~~")
            exit()

        # if the user enters an option number not presented in the Menu Option, the program closes
        else:
            print("\n~~ Invalid Choice Option ~~")
            print("   Closing WGUPS")
            exit()
    # catches invalid input and closes the program
    except ValueError:
        print("\n~~ Invalid input ~~")
        print("   Closing WGUPS")
        exit()
