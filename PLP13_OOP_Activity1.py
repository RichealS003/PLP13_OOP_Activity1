class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date
        #I added the variable here so if it was required later in the code for any arithmetic operation, it will be easy to access it.
        self.weight_allowance = 20

    def get_passenger_info(self):
        return f"Passenger: {self.name}\nLocation: {self.location}\nDestination: {self.destination}\nDate:{self.date}"

    def get_weight_allowance(self):
        return f"Allowed default weight is {self.weight_allowance} kg."


# passenger = Passenger("Marcus","Atlanta","Ghana","25th September 2026")
# print(passenger.get_passenger_info())
# print(passenger.get_weight_allowance())