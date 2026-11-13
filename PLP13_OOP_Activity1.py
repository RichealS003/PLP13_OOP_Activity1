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



class first_class(Passenger):
    def __init__(self, name, location, destination, date, ticket_class, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        self.ticket_class = "First Class"
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service

    def get_passenger_info(self):
        return ( f"{super().get_passenger_info()}\n"  f"Suite Number: {self.suite_number}\n" f"Chaffeur Service: {self.chauffeur_service}" )




# passenger = Passenger("Marcus","Atlanta","Ghana","25th September 2026")
# print(passenger.get_passenger_info())
# print(passenger.get_weight_allowance())