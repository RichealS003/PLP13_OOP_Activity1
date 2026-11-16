class InvalidPassengerData(Exception):
    """Raised when passenger details are missing or invalid."""
    pass


class Passenger:
    def __init__(self, name, location, destination, date):
        if not name or not location or not destination or not date:
            raise InvalidPassengerData("Name, location, destination and date are required.")
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date
        self.weight_allowance = 20

    def get_passenger_info(self):
        return f"Passenger: {self.name}\nLocation: {self.location}\nDestination: {self.destination}\nDate: {self.date}"

    def get_weight_allowance(self):
        return f"Allowed default weight is {self.weight_allowance} kg."


class first_class(Passenger):
    def __init__(self, name, location, destination, date, ticket_class, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        if not suite_number:
            raise InvalidPassengerData("Suite number is required for First Class.")
        self.ticket_class = "First Class"
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service

    def get_passenger_info(self):
        return (f"{super().get_passenger_info()}\n"
                f"Suite Number: {self.suite_number}\n"
                f"Chauffeur Service: {self.chauffeur_service}")


class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        if not seat_preference:
            raise InvalidPassengerData("Seat preference is required for Economy.")
        self.seat_preference = seat_preference

    def get_passenger_info(self):
        return f"{super().get_passenger_info()}\nSeat Preference: {self.seat_preference}"


class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        if not lounge_pass_code:
            raise InvalidPassengerData("Lounge pass code is required for Business.")
        self.lounge_pass_code = lounge_pass_code
        self.weight_allowance = 100

    def get_passenger_info(self):
        return f"{super().get_passenger_info()}\nLounge Pass Code: {self.lounge_pass_code}"


def create_passenger(choice, details):
    try:
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
        else:
            raise InvalidPassengerData("Invalid class choice. Use 1, 2 or 3.")
    except KeyError as e:
        raise InvalidPassengerData(f"Missing detail: {e}")


def print_ticket_summary(passenger, choice):
    print("FLIGHT TICKET SUMMARY")
    print("Passenger :", passenger.name)
    print("From      :", passenger.location)
    print("To        :", passenger.destination)
    print("Date      :", passenger.date)

    try:
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
    except AttributeError:
        print("Error: the class choice doesn't match this passenger.")

    print("Baggage   :", passenger.weight_allowance, "kg")
