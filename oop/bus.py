from vehicle import Vehicle

class Bus(Vehicle):
    # top_speed = 100 #Attribute or Variable
    # warnings = []

    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus1 = Bus(150)
bus1.add_warnings('Test')
bus1.add_group(['Sri', 'Hari', 'Sara', 'Sam'])
print(bus1.passengers)

bus1.drive()