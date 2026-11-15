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
        return ( f"{super().get_passenger_info()}\n"  f"Suite Number: {self.suite_number}\n" f"Chauffeur Service: {self.chauffeur_service}" )


class Economy(Passenger):
    """Represents an economy class passenger.
    Adds a seat preference. Uses the default 20kg weight allowance."""
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_passenger_info(self):
        return (f"{super().get_passenger_info()}\n"
                f"Seat Preference: {self.seat_preference}")


class Business(Passenger):
    """Represents a business class passenger.
    Adds a lounge pass code. Overrides weight allowance to 100kg."""
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code
        self.weight_allowance = 100

    def get_passenger_info(self):
        return (f"{super().get_passenger_info()}\n"
                f"Lounge Pass Code: {self.lounge_pass_code}")

# passenger = Passenger("Marcus","Atlanta","Ghana","25th September 2026")
# print(passenger.get_passenger_info())
# print(passenger.get_weight_allowance())



def create_passenger(choice, details):
    name = details["name"]
    location = details["location"]
    destination = details["destination"]
    date = details["date"]

    if choice == "1":
        return Economy(name, location, destination, date, details["seat_preference"])
    elif choice == "2":
        return Business(name, location, destination, date, details["lounge_pass_code"])
    elif choice == "3":
        return first_class(name, location, destination, date, "First Class",
                           details["suite_number"], details["chauffeur_service"])


def print_ticket_summary(passenger, choice):
    print("FLIGHT TICKET SUMMARY")
    print("Passenger :", passenger.name)
    print("From      :", passenger.location)
    print("To        :", passenger.destination)
    print("Date      :", passenger.date)

    if choice == "1":
        print("Class     : Economy")
        print("Seat      :", passenger.seat_preference)
    elif choice == "2":
        print("Class     : Business")
        print("Lounge    :", passenger.lounge_pass_code)
    elif choice == "3":
        print("Class     : First Class")
        print("Suite     :", passenger.suite_number)
        if passenger.chauffeur_service:
            print("Chauffeur : Yes")
        else:
            print("Chauffeur : No")

    print("Baggage   :", passenger.weight_allowance, "kg")
