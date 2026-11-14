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

CLASS_MAP = {
    "1": (Economy, "Economy", ["seat_preference"], {}),
    "2": (Business, "Business", ["lounge_pass_code"], {}),
    "3": (first_class, "First Class", ["suite_number", "chauffeur_service"],
          {"ticket_class": "First Class"}),
}
 
 
def create_passenger(choice, details):
    cls, _label, extras, fixed = CLASS_MAP[choice]
    base = {k: details[k] for k in ("name", "location", "destination", "date")}
    extra = {k: details[k] for k in extras}
    return cls(**base, **extra, **fixed)
 
 
def print_ticket_summary(passenger, choice):
    _cls, label, extras, _fixed = CLASS_MAP[choice]
    rows = [
        ("Passenger", passenger.name),
        ("From", passenger.location),
        ("To", passenger.destination),
        ("Date", passenger.date),
        ("Class", label),
    ]
    for attr in extras:
        value = getattr(passenger, attr)
        if isinstance(value, bool):
            value = "Yes" if value else "No"
        rows.append((attr.replace("_", " ").title(), value))
    rows.append(("Baggage Allowance", f"{passenger.weight_allowance} kg"))
 
    width = max(len(k) for k, _ in rows)
    line = "=" * (width + 28)
    print(line)
    print("FLIGHT TICKET SUMMARY".center(len(line)))
    print(line)
    for key, value in rows:
        print(f"{key:<{width}} : {value}")
    print(line)



# passenger = Passenger("Marcus","Atlanta","Ghana","25th September 2026")
# print(passenger.get_passenger_info())
# print(passenger.get_weight_allowance())
