class House:
    num_houses = 0
    def __init__(self, address, no_floors, no_rooms, heating_type):
        self.address = address
        self.no_floors = no_floors
        self.no_rooms = no_rooms
        self.heating_type = heating_type
        House.num_houses += 1
        House.__str__(self)
    def __str__(self):
        print(f"The address of the house is {self.address}, "
              f"it has {self.no_floors} "
              f"floors and {self.no_rooms} "
              f"rooms, its heating type is {self.heating_type}")

    @classmethod
    def no_of_houses(cls):
        return cls.num_houses


user_house = House("Dowland Park", 5, 2, "oil")
print(House.no_of_houses())