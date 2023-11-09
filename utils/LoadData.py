import csv
from HashTable import HashTable

from Package import Package


# This method opens and reads the packages csv file into a 2D array list by accepting the file name as a parameter.
# Then, with the data from the list, instances of Package objects are created and inserted into the hash table
# Returns an instance of the hash table
# Run-time complexity: O(n)
def load_package(filename):
    hash_table = get_hash()  # hash table instance
    file = open(filename, "r")  # opens the file for reading
    csv_package = list(csv.reader(file, delimiter=","))  # inserts file data into a 2D array list
    for package in csv_package:  # for each row (package) in the list, assigns a value for the attribute (if any)
        package_id = int(package[0])
        delivery_address = package[1]
        delivery_city = package[2]
        delivery_state = package[3]
        delivery_zip = package[4]
        deadline = package[5]
        weight = package[6]
        delivery_notes = package[7]
        # package object
        package_info = Package(package_id, delivery_address, " ", delivery_city, delivery_state, delivery_zip, deadline,
                               weight, delivery_notes, "At Hub", " ", " ", " ")
        # inserts package objects into the hash table
        hash_table.insert_item(package_id, package_info)

    return hash_table


# Gets an instance of hash table
def get_hash():
    hash_table = HashTable()
    return hash_table


# This method opens and reads the distance csv file into a 2D array list by accepting the file name as a parameter
# Returns the 2D array list of distances
# Run-time complexity : O(n)
def load_distance(filename):
    csv_distance = []
    file = open(filename, "r")
    distance_reader = csv.reader(file, delimiter=",")
    for row in distance_reader:
        csv_distance.append(row)
    return csv_distance


# This method opens and reads the distance csv file into a 2D array list by accepting the file name as a parameter
# Returns the 2D array list of addresses
# Run-time complexity: O(n)
def load_address(filename):
    csv_address = []
    file = open(filename, 'r')
    address_reader = csv.reader(file, delimiter=",")
    for row in address_reader:
        csv_address.append(row)
    return csv_address
