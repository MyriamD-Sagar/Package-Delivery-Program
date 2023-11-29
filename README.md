# Package-Delivery-Program


The purpose of this project is to create a Python application that simulates the delivery of 40 packages while considering a large set of constraints.

This project was completed for the Data Structures and Algorithms II - C950 course at WGU.

Students were given a scenario where the Western Governors University Parcel Service (WGUPS) needed to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD).
The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements. 

## Programming Language

The programming language used is Python (version 3.10). Python is an interpreted, object-oriented, dynamic high-level programming language.

## OS

The operating system running on my local machine (PC) is a 64-bit Windows 10 operating system.

## IDE

The integrated development environment (IDE) used to write, modify, and test the code is PyCharm Community Edition 2022.1.
PyCharm allowed me to import data directly from my local machine (e.g., csv files) and to structure this data to use it meaningfully in my program.
PyCharm also makes it possible for the user to run the Python program from within the IDE. This environment provides useful standard libraries, which makes coding easier.

## Constraints

* Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
* The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
* There are no collisions.
* Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
* Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
* The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
* There is up to one special note associated with a package.
* The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
  WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m.
  However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
* The distances provided in distances.csv are equal regardless of the direction traveled.
* The day ends when all 40 packages have been delivered.
