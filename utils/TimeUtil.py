import datetime


# This method converts a string of format hh:mm:ss to datetime type
# I was able to find this conversion after multiple errors and trials by consulting <datetime module> on python.org
# Returns the time as timedelta (to allow comparison operation)
def string_to_datetime(time):
    time_delta = datetime.datetime.strptime(time, '%H:%M:%S')  # parses the string
    time_split_delta = datetime.timedelta(hours=time_delta.hour, minutes=time_delta.minute, seconds=time_delta.second)
    return time_split_delta


# This method was created to assign a string value to the package's delivery status
# It receives as parameters three times of type datetime (timedelta)
# The user input time is compared to the package departure time and delivery time to determine the status of the package
# Returns the status of the package at the time chosen by the user (user_time)
def verify_time(package_departure_time, package_delivery_time, user_time):
    if package_departure_time <= user_time < package_delivery_time:
        status = 'En Route'
    elif user_time >= package_delivery_time:
        status = 'Delivered'
    else:
        status = 'At Hub'

    return status

