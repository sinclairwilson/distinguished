class Car:
    # Define Car Tuple made up of Make, Model, Reg, Rental Group and Cost per Day
    def __init__(self, make, model, registration_number, rental_group, cost_per_day):
        self.make = make
        self.model = model
        self.registration_number = registration_number
        self.rental_group = rental_group
        self.cost_per_day = cost_per_day
