import argparse, paho.mqtt.client as mqttClient
from os import system
#from tabulate import tabulate
#from tinydb import TinyDB, Query
#import pandas as pd
from datetime import datetime
import sys, time


# class ParkingLot:

"""    def __init__(self, number_of_slots: int):
        self.db = TinyDB('../db/tiny_db.json')  # Initialize the local db
        self.db.truncate()  # Clear DB
        self.number_of_parking_slots = number_of_parking_slots  # Set number of parking slots
        for index in range(number_of_slots):  # Set all slots to be vacant
            self.db.insert({'Parking Lot': index+1, 'Occupancy': 'VACANT', 'Vehicle': '-'})

    def print_occupancy(self):  # Print the parking slot occupancy information
        print(tabulate(pd.DataFrame(self.db.all()), headers='keys', tablefmt='psql',
                       showindex=False, colalign=("center", "center", "center")))"""

Connected = False
ground_sensor_count = 10
ground_sensor_list = [f"smartparking/groundsensor/slot-{index+1}" for index in range(ground_sensor_count)]
parking_slot_occupancy = [0] * ground_sensor_count
request_topic = f'smartparking/findcarbyplatedetails/request'
response_topic = f'smartparking/findcarbyplatedetails/response'

# on_connect method for the MQTT client
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Connected to broker")
        global Connected # Use global variable
        Connected = True # Signal connection
    else:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Connection failed Return Code : {rc}")


def on_message(client, userdata, message):
    global parking_slot_occupancy
    topic_type = str(message.topic).split('/')[1]
    payload = message.payload.decode("utf-8")
    if topic_type == 'groundsensor':
        slot_name = str(message.topic).split('/')[2]
        slot_id = int(slot_name.split('-')[1])
        parking_slot_occupancy[slot_id-1] = int(payload.strip())
        # print(parking_slot_occupancy)
    else:
        print(payload)


if __name__ == "__main__":
    # Setup MQTT client configuration
    client_name = 'Gateway'
    client = mqttClient.Client(client_name)
    broker_address, port = "127.0.0.1", 1883  # Broker address, port
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message  # attach function to callback
    client.connect(broker_address, port=port)  # connect to broker

    client.loop_start()  # start the loop
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - client_name is ****{client_name}****")

    # Subscribing to ground sensors
    for each_client in ground_sensor_list:
        client.subscribe(each_client)

    client.subscribe(response_topic)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Subscribed to all ground sensors")
    """
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('parking_slots', help='Number of parking slots')
    args = my_parser.parse_args()
    number_of_parking_slots = int(args.parking_slots)
    parking_lot = ParkingLot(number_of_parking_slots)
    """
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
            #parking_lot.print_occupancy()
            print("Free slots available - ", [f"slot-{x+1}" for x in range(ground_sensor_count) if int(parking_slot_occupancy[x]) == 1])
        elif user_input == '2':
            user_input = input("Enter last four digits of plate number ")
            client.publish(request_topic,user_input.strip())
            time.sleep(2)
        else:
            print("Invalid Input - Available options are listed at the top")
        _ = input("Press enter to continue\n")
