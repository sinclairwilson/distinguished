from datetime import date


class Renter:
    # Define Renter as Tuple last_name, first_name, DLN, DOB
    def __init__(self, last_name, first_name, driving_license_number, date_of_birth):
        self.last_name = last_name
        self.first_name = first_name
        self.driving_license_number = driving_license_number
        self.date_of_birth = date_of_birth
