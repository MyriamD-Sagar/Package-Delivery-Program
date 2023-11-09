# Ref: C950 Supplemental Resource. WGU C950- Webinar- 1- Let's Go Hashing - Complete Python Code
# The complete reference can be found in pdf document in part L

# This class defines the hash table
# This hash table is the data structure that will be used to store and retrieve Package objects
# Space complexity : O(n)
class HashTable:
    # constructor of the HashTable class
    def __init__(self, capacity=40):
        self.hash_table = []
        for i in range(capacity):
            self.hash_table.append([])

    # Method used to insert package object into the hash table
    # Run-time complexity: O(n)
    def insert_item(self, key, item):
        slot = hash(key) % len(self.hash_table)
        slot_list = self.hash_table[slot]
        for k in slot_list:
            if k[0] == key:
                k[1] = item
                return True
        key_value_pair = [key, item]
        slot_list.append(key_value_pair)
        return True

    # Method used to get a package object that matches a given key (package ID)
    # Run-time complexity: O(1)
    def get_item(self, key):
        slot = hash(key) % len(self.hash_table)  # hash code to get the slot corresponding to the key
        slot_list = self.hash_table[slot]
        for k in slot_list:  # searches through the slot list to find the item that matches the key
            if k[0] == key:
                return k[1]  # returns the package object if found
            return None  # returns nothing if key is not found
