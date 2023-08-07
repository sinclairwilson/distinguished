# Car Rental System

Developer: Wilson Sinclair 

[wilson.sinclair@gmail.com](mailto:wilson.sinclair@gmail.com)

Last Update: 7-8-23

### Description

This is a project that has been created to deliver a new Car Rental Solution.

The project will deliver three capabilities based on requirements delivered to our development team by our car rental client.

The three user stories are based on two personas, that of the car rental company and that of the car renter.

***

### User Stories

#### 1. Finding a car to rent

As a car rental company we want to match the potential renter to a car that we have to rent

#### 2. Finding an available car to be rented

As a car renter I want to know if a car is available to be rented on the dates I need.

This will provide the ability to provide the car renter will a list of cars that are available on the dates given by the renter

#### 3. Booking a car

As a car renter I want to book a car which has been shown to me as being available

This will provide a car available to me during the rental period

***

### Technical Implementation Details

#### 1. Data Model

As this is a iterative project, Python data types have been used to create a Minimum Viable Product (MVP)
to demonstrate the initial design.

| Class Name | Description   | Field Names                                                  | filename  |
|------------|---------------|--------------------------------------------------------------|-----------
| Car        | Rental car    | Make,Model,Registration Number, Rental Type, Cost Per Day    | Car.py    |
| Renter     | Renter of car | Last Name, First Name, Driving Licence Number, Data of Birth | Renter.py |
