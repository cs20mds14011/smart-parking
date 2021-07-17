import argparse
from os import system
from tabulate import tabulate
from tinydb import TinyDB, Query
import pandas as pd


class ParkingLot:

    def __init__(self, number_of_slots: int):
        self.db = TinyDB('../db/tiny_db.json')  # Initialize the local db
        self.db.truncate()  # Clear DB
        self.number_of_parking_slots = number_of_parking_slots  # Set number of parking slots
        for index in range(number_of_slots):  # Set all slots to be vacant
            self.db.insert({'Parking Lot': index+1, 'Occupancy': 'VACANT', 'Vehicle': '-'})

    def print_occupancy(self):  # Print the parking slot occupancy information
        print(tabulate(pd.DataFrame(self.db.all()), headers='keys', tablefmt='psql',
                       showindex=False, colalign=("center", "center", "center")))


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('parking_slots', help='Number of parking slots')
    args = my_parser.parse_args()
    number_of_parking_slots = int(args.parking_slots)
    parking_lot = ParkingLot(number_of_parking_slots)
    screen_prompt = "\t\tSmart Parking User Interface\n" \
                    "-------------------------------------------------------------------\n\n" \
                    "Press 1 for listing free parking slots\n" \
                    "Press 2 for searching a car by its plates\n"\
                    "Press 0 to exit\n\n\n" \
                    "Key Input:" \
                    ""
    while True:
        _ = system("clear")
        user_input = input(screen_prompt)
        if user_input == '0':
            user_input = input("Are you sure you want to exit? Y/N")
            if user_input.strip().upper() == 'Y':
                break
        elif user_input == '1':
            parking_lot.print_occupancy()
        elif user_input == '2':
            print("Under construction")
        else:
            print("Invalid Input - Available options are listed at the top")
        _ = input("Press enter to continue\n")
