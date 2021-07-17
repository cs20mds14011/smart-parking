# Start ground sensors
nohup python ground_sensor.py 1 ../data/ground_sensor.txt &
nohup python ground_sensor.py 2 ../data/ground_sensor.txt &
nohup python ground_sensor.py 3 ../data/ground_sensor.txt &
nohup python ground_sensor.py 4 ../data/ground_sensor.txt &
nohup python ground_sensor.py 5 ../data/ground_sensor.txt &
nohup python ground_sensor.py 6 ../data/ground_sensor.txt &
nohup python ground_sensor.py 7 ../data/ground_sensor.txt &
nohup python ground_sensor.py 8 ../data/ground_sensor.txt &
nohup python ground_sensor.py 9 ../data/ground_sensor.txt &
nohup python ground_sensor.py 10 ../data/ground_sensor.txt &

# Start camera sensor
nohup python camera_sensor.py ../data/camera_sensor.txt &

# Start Gateway
python Gateway.py
