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

| Class Name       | Description          | DataType | Field Names                                                  | filename            |
|------------------|----------------------|----------|--------------------------------------------------------------|---------------------
| Car              | Rental car           | Tuple    | Make,Model,Registration Number, Rental Type, Cost Per Day    | Car.py              |
| Renter           | Renter of car        | Tuple    | Last Name, First Name, Driving Licence Number, Data of Birth | Renter.py           |
| Criteria         | Criteria for booking | Tuple    | Rental Group, Start Date, End Date                           | Criteria.py         |
| CarRentalCompany | Car Rental Instance  | List     | Lists of Cars available for rent and already rented          | CarRentalCompany.py |

#### 2. Design Assumptions - Story 1

The project assumes initially there would a web client that customers would interact with.

The web client would allow potential renters would submit their queries and book cars.

The file CarRental.py is the instance of creating the inital list of cars and current renters.

For the Acceptance criteria, to return a list of matching cars - the code only considers the availability of cars using the Rental Type.

```
        criteria = Criteria()
        cars_available = car_rental_company.matching_cars(rental_group, NULL, NULL)

```
In CarRentalCompany.py the matching_cars function interates through to create a list of cars matching the Rental Type criteria.

The design criteria discusses the need for the ability for the implementation to be threadsafe i.e. allow it to be called from multiple threads.

Although documenation says that Python honours updates that are threadsafe, 
noting these calls could be coming via an API, the MVP has proposed use of basic lockimg.

As is seen in CarRental.py, using Python's standard Threading library:

```
    import threading
    ....
    ....
    lock = threading.Lock()

    with lock:
        car_rental_company.add_car(self.CAR1)
        car_rental_company.add_car(self.CAR2)
        car_rental_company.add_car(self.CAR3)
        car_rental_company.add_car(self.CAR4)

```
#### 3. Design Assumptions - Story 2 and Story 3

In order to determine the availability of cars available on a current date for a given rental type
it's expected to build on the list created in Story 1 of all cars of a certain rental type.

In CarRental.py the code would create a list of rental cars currently rented against a rental period.

```
        self.rentals = [] # Current cars booked out by customers
        ....
        ....
```

For Story 3, the functions in CarRentalCompany.py would manipulate the lists cars and rentals using
the functions rent_car and return_car. This code would need to adopt threadsafe approaches as detailed in Story 2.

The querying of cars that match the crieria in Story 2 is yet to be developed.


#### 4. Testing

The implementation assumes a Test Driven Approach with unit tests created to ensure that at all stages of Development
the underlying code will be thoroughly tested against know data criteria.

| filename           | Description                                               |
|-----------------------|-----------------------------------------------------------|
| CarRentalTest.py      | Testing full functionality of solution                    |
| DatePeriodTest.py     | Specific tests associated with submission of date periods |
| DatePeriodUtilTest.py | Testing of functions created for date period manipulation |


#### 5. Future Considerations

As this is a iterative project, simple Python types have been used to create the MVP.

Longer term there would need to be considerations for a more industrial design, to include:

* Database to store all key information - this could be a relational database or document store. 
Both would provide a more robust transction data model and other benefits such as backup/recovery


* API interfaces to present all interfaces to data services


* Multiple client options - a more robust data store would also support longer term multiple clients including a web and mobile app