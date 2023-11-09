from utils import LoadData


# This method gets the address id (index) by searching the 2D array list (address_list).
# It loads the array from the python file LoadData by calling the method load_address().
# Then, it searches for the row that contains the address in index position 2 (row[2]) received as parameter.
# Returns the value found in index position 0 of that row, which is the address id.
# Run-time complexity: O(n)
def find_address_index(address):
    address_list = LoadData.load_address('csvFiles/addresses.csv')
    value = address
    for target_row in address_list:
        if value in target_row[2]:
            return int(target_row[0])


# This method gets a distance between two addresses.
# It loads the array from the python file LoadData by calling the load_distance() method.
# It gets the index of the addresses received as parameters by calling find_address_index()
# It assigns the first address index as the row and the second as the index of that row
# Returns the value found at that position.
# Run-time complexity: O(1)
def find_distance(address_1, address_2):
    distance_list = LoadData.load_distance('csvFiles/distances.csv')
    index_address_1 = find_address_index(address_1)
    index_address_2 = find_address_index(address_2)
    distance = distance_list[index_address_1][index_address_2]
    # if the value found is empty, value is the same as if we reverse the addresses indexes (ids)
    if distance == '':
        distance = distance_list[index_address_2][index_address_1]
    return float(distance)


# This method finds the closest address in the list of package ID (second parameter) to the address (first parameter).
# It loads the hash table from the python file LoadData by calling the method load_package().
# It loops the function call get_item() by passing each id in the list as a parameter.
# It gets the address of the package associated with the id to call the method find_distance() to get the distance.
# Returns the address of the package with the smallest distance from current_address.
# Run-time complexity: O(n)
def find_closest_address(current_address, package_list):
    hash_table = LoadData.load_package('csvFiles/packages.csv')
    min_distance = 1000.0
    closest_address = " "
    for id in package_list:
        package = hash_table.get_item(id)  # run-time complexity of O(1)
        package_address = package.delivery_address
        distance = find_distance(current_address, package_address)  # run-time complexity of O(1)
        if distance < min_distance:
            min_distance = distance
            closest_address = package_address
    return closest_address


