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


# function to selsct ticket class using input & conditionals 
def get_ticket_class():
    print("\n Welcome to Group 13 airlines")
    print("[1] Economy")
    print("[2] Business")
    print("[3] First Class")
    
    choice = input("Select your class (1/2/3): ")
    
    if choice == "1":
        return "1"
    elif choice == "2":
        return "2"
    elif choice == "3":
        return "3"
    else:
        return "1"  

# function to collect common details and then class specific fields
def collect_passenger_details():
    print("\n Flight Details")
    name = input("Name: ")
    location = input("From: ")
    destination = input("To: ")
    date = input("Date (example: 2026-11-13): ")
    
    choice = get_ticket_class()

    #storing the details in a dict 
    details = {
        "name": name,
        "location": location,
        "destination": destination,
        "date": date,
        "choice": choice,   
    }  
    
    if choice == "1":
        details["seat_preference"] = input("Seat preference (window/aisle/middle): ")
    elif choice == "2":
        details["lounge_pass_code"] = input("Lounge pass code: ")
    elif choice == "3":
        details["suite_number"] = input("Suite number: ")
        chauffeur = input("Chauffeur service? (yes/no): ").lower() == "yes"
        details["chauffeur_service"] = chauffeur
    
    return details

# passenger = Passenger("Marcus","Atlanta","Ghana","25th September 2026")
# print(passenger.get_passenger_info())
# print(passenger.get_weight_allowance())
