# 1_Create a class Vehicle with Attributes: name, max_speed, and total_capacity.
# Method: fare. It should calculate the price of the trip. Formula: total_capacity * 100

class Vehicle:

    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self, total_capacity):
        return self.total_capacity * 100


# Process finished with exit code 0

# 2_Create classes Bus and Car that inherit Vehicle.

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    pass


class Car(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    pass


# Process finished with exit code 0

# 3_Create 3 car objects and 2 bus objects

car_1 = Car('Suzuki', 150, 5)
car_2 = Car('Volkswagen', 180, 5)
car_3 = Car('Mazda', 200, 7)
bus_1 = Bus('Iveco', 129, 15)
bus_2 = Bus('Urbino', 120, 27)

# Process finished with exit code 0

# 4_Check: if car_1 is instance of Car.  if car_2 is instance of Vehicle. if bus_1 is instance of Car.
# if bus_1 is instance of Vehicle.

print(f"car_1 is instance of Car - {isinstance(car_1, Car)}")  # car_1 is instance of Car - True
print(f"car_2 is instance of Vehicle - {isinstance(car_2, Vehicle)}")  # car_2 is instance of Vehicle - True
print(f"bus_1 is instance of Car - {isinstance(bus_1, Car)}")  # bus_1 is instance of Car - False
print(f"bus_1 is instance of Vehicle - {isinstance(bus_1, Vehicle)}")  # bus_1 is instance of Vehicle - True


# 5_5 Override fare method for Bus class. Here we need to add an extra 10% to the fare.
# Formula: total_fare + 10% of total_fare.

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    def fare(self, total_capacity):
        return total_capacity * 100 * 1.1


# Process finished with exit code 0

# 6_Add used_capacity attribute for Bus. It means how many people are on the bus.
# If used_capacity > total_capacity raise an error.
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity

    def get_used_capacity(self, used_capacity):
        if used_capacity > self.total_capacity:
            print(f"Error! Used_capacity  should not be more than {self.total_capacity}")
        else:
            self.used_capacity = used_capacity

    def fare(self, total_capacity):
        return total_capacity * 100 * 1.1


# Process finished with exit code 0

# 7_Write a magic method to Bus that would be triggered when len() function is called.

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity

    def set_used_capacity(self, used_capacity):
        if used_capacity > self.total_capacity:
            print(f"Error! Used_capacity  should not be more than {self.total_capacity}")
        else:
            self.used_capacity = used_capacity

    def fare(self, total_capacity):
        return total_capacity * 100 * 1.1

    def __len__(self):
        return len(self.name)

    def __gt__(self, other):
        return len(self) > len(other)


# Process finished with exit code 0

# 8_Create class Engine with attribute volume and method get_volume() that will return volume.
# 9_Inherit Engine by Car class.
class Engine(Car):
    def __init__(self, name, max_speed, total_capacity, volume):
        super().__init__(name, max_speed, total_capacity)
        self.volume = volume

    def get_volume(self):
        return self.volume


# Process finished with exit code 0

# 10_Check what is inheritance order of the Car class

print(f"Engine is inherit of Car - {issubclass(Engine, Car)}")

# Engine is inherit of Car - True
