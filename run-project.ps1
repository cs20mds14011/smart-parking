
# Start ground sensors
start powershell "python.exe ground_sensor.py 1 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 2 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 3 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 4 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 5 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 6 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 7 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 8 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 9 ../data/ground_sensor.txt"
start powershell "python ground_sensor.py 10 ../data/ground_sensor.txt"

# Start camera sensor
start powershell "python camera_sensor.py ../data/camera_sensor.txt"

# Start Gateway
start powershell "python Gateway.py"