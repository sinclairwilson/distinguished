import threading
from datetime import date
from main.rental.Renter import Renter
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.CarRentalCompany import CarRentalCompany
from threading

# Create set of tuples that define current list of cars

    CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)
    CAR2 = Car("VW", "Passat", "XX12 2UR", "C1", 110)
    CAR3 = Car("VW", "Polo", "XX13 3UR", "A1", 65)
    CAR4 = Car("VW", "Polo", "XX14 4UR", "A1", 70)

# Create set of tuples that define current renters

    RENTER1 = Renter("Hydrogen", "Joe", "HYDRO010190JX8NM", date(1990, 1, 1))
    RENTER2 = Renter("Calcium", "Sam", "CALCI010203SX8NM", date(2003, 2, 1))
    RENTER3 = Renter("Neon", "Maisy", "NEONN010398MX8NM", date(1998, 3, 1))
    RENTER4 = Renter("Carbon", "Greta", "CARBO010497GX8NM", date(1997, 4, 1))

# Create new instance of CarRentalCompany  and then add cars to this list
# Although modern Python 3.x list management is thread safe better to be safe than sorry


    car_rental_company = CarRentalCompany()

# Although modern Python 3.x list management is thread safe better to be safe than sorry
# Acquire lock and carry out updates in block with lock

    lock = threading.Lock()

    with lock:
        car_rental_company.add_car(self.CAR1)
        car_rental_company.add_car(self.CAR2)
        car_rental_company.add_car(self.CAR3)
        car_rental_company.add_car(self.CAR4)

# Criteria would likely come from web or mobile app - criteria are Rental Group
# This first stage query does not consider the availability of the cars in time
# rental_group would be set by user interface - Story 1

        criteria = Criteria()
        cars_available = car_rental_company.matching_cars(rental_group, NULL, NULL)



# Need to create a permanent record of what cars and what renters are booked out against a day
# Create a list of records that is [CAR, RENTER, START_DATE, END_DATE] - Story 2 and 3
# START_DATE, END_DATE are assumed to be of type timeperiod










