import ast
import math
import sys
import time

import paho.mqtt.client as mqttClient

IsSlotOccupied=0
Connected = False
hq_address = "127.0.0.1"
port = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    Global IsSlotOccupied
    #IsSlotOccupied = next(fp).strip("\n").strip()
    print(IsSlotOccupied)
    client.publish('location/HQ_receive_1', IsSlotOccupied)



slot_name_client = sys.argv[1]
slot_name = sys.argv[1]
print(f'Sensor:{slot_name}')



client = mqttClient.Client(slot_name_client)  # create new instance
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(hq_address, port=port)  # connect to HQ

client.loop_start()  # start the loop

slot_topic = "smartparking/groundsensor/" + slot_name


client.subscribe(slot_topic)

try:
    with open(f'../data/{slot_name}.txt','r') as fp:
        IsOccupied = fp
        time.sleep(2)
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
finally:
    if not fp.closed:
        fp.close()
