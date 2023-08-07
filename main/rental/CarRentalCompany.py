class CarRentalCompany:
    def __init__(self):
        self.cars = [] # Define List to hold Cars held by company
        self.rentals = [] # Current cars booked out by customers

    def add_car(self, car): # Function to add car to List
        self.cars.append(car)

    def matching_cars(self, *args): # Function to check matching status of cars

        # Iterate through list type matching criteria
        matching_list = []
        for x in cars:
            if arg[0] in x:
            matching_list.append[x]

        return matching_list

    def rent_car(self, renter, car, timeperiod):
        # Add car to rentals list
        self.rentals.append(renter,car, timeperiod)
        return rentals

    def return_car(self, renter, car, timeperiod):
        # Remove car from rentals list
        # Move car to cars available list
        self.rentals.remove(car)
        self.cars.append
        return rentals
