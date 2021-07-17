import ast, math, sys, time, paho.mqtt.client as mqttClient

IsSlotOccupied=0
Connected = False
hq_address = "127.0.0.1"
port = 1883

# on_connect method for the MQTT client
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Connected to broker")
        global Connected # Use global variable
        Connected = True # Signal connection
    else:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Connection failed Return Code : {rc}")

parking_sensor_id = sys.argv[1]
slot_name = f"slot-{parking_sensor_id}"
sensor_data_file = sys.argv[2]

client = mqttClient.Client(slot_name)  # create new instance
client.on_connect = on_connect  # attach function to callback
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - client_name is ****{client_name}****")

client.connect(hq_address, port=port)  # connect to HQ
client.loop_start()  # start the loop
slot_topic = "smartparking/groundsensor/" + slot_name
client.subscribe(slot_topic)
       
with open(sensor_data_file, 'r') as sensor_data:
    sensor_status = int(sensor_data.read().strip().split()[parking_sensor_id-1])
    client.publish(f"location/{client_name}", sensor_status)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Publishing ground sensor information to Gateway")
    time.sleep(5)
