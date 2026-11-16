VIDEO LINK - https://drive.google.com/file/d/1DMImNlJv7GVDX8JNBeklhZAPPUIgWl7q/view?usp=drive_link


# Passenger Flight Ticket System

## Project Overview

The Passenger Flight Ticket System is a Python-based program designed to represent passengers travelling by air under different ticket classes: Economy, Business, and First Class.

The program uses **Object-Oriented Programming (OOP)** concepts, particularly classes, inheritance, constructors, method overriding, and the `super()` function, to organize passenger information and class-specific services.

## Features

- Stores passenger details, including name, location, destination, and travel date.
- Supports three passenger categories:
  - Economy Class
  - Business Class
  - First Class
- Assigns baggage allowances based on passenger class.
- Stores additional services and preferences specific to each ticket class.
- Generates passenger information summaries.
- Prints flight ticket summaries with passenger and baggage details.
- Uses inheritance to reduce code repetition and promote code reusability.

## Class Structure

### 1. Passenger (Parent Class)

The `Passenger` class serves as the parent class for all passenger categories.

It stores the common passenger information:

- Name
- Location
- Destination
- Travel date
- Default baggage allowance of 20 kg

**Methods:**
- `get_passenger_info()` – Returns the passenger's general information.
- `get_weight_allowance()` – Returns the passenger's default baggage allowance.

### 2. Economy (Child Class)

The `Economy` class inherits from `Passenger`.

It introduces an additional attribute:

- Seat preference

Economy passengers retain the default baggage allowance of 20 kg.

It also overrides `get_passenger_info()` to include the passenger's seat preference.

### 3. Business (Child Class)

The `Business` class inherits from `Passenger`.

It introduces an additional attribute:

- Lounge pass code

Business passengers receive a baggage allowance of 100 kg.

It overrides `get_passenger_info()` to include the lounge pass code.

### 4. first_class (Child Class)

The `first_class` class inherits from `Passenger`.

It introduces the following attributes:

- Suite number
- Chauffeur service

It overrides `get_passenger_info()` to include the passenger's suite number and chauffeur service information.

It currently retains the default baggage allowance of 20 kg inherited from the parent class.

## Main Functions

### `create_passenger(choice, details)`

Creates and returns a passenger object based on the selected ticket class.

| Choice | Passenger class |
|---|---|
| 1 | Economy |
| 2 | Business |
| 3 | First Class |

The function retrieves the required passenger information from a dictionary and passes it to the appropriate class constructor.

An invalid choice raises a `ValueError`.

### `print_ticket_summary(passenger, choice)`

Displays a flight ticket summary containing:

- Passenger name
- Departure location
- Destination
- Travel date
- Ticket class
- Class-specific information
- Baggage allowance

The displayed information depends on the passenger's selected ticket class.

## Object-Oriented Programming Concepts Used

**Inheritance:** Economy, Business, and first_class inherit common attributes and methods from Passenger.

**Encapsulation:** Passenger information and class-specific attributes are organized within their respective classes.

**Polymorphism:** Each child class overrides `get_passenger_info()` to provide information specific to its passenger category.

**Code Reusability:** The `super()` function allows child classes to reuse the parent class constructor and passenger information method.

## Requirements

- Python 3.x
- No external libraries are required. The program uses Python's built-in features.

## Running the Program

Save the Python code in a file, for example:

`passenger_ticket.py`

Run it from your terminal using:

```bash
python passenger_ticket.py
```

**Note:** The submitted code currently defines the classes and functions but does not yet include a complete interactive menu or function calls to collect passenger details and generate a ticket automatically.

## Project Purpose

This project demonstrates the practical application of Python Object-Oriented Programming through a flight ticket management scenario. It focuses on using inheritance, class-specific attributes, method overriding, and reusable functions to organize passenger information efficiently.

---

**Technologies Used:** Python 3  
**Project Type:** Object-Oriented Programming  
**Domain:** Airline and Passenger Management
