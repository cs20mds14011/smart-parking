<h1> Smart Parking - IOT Project </h1>


<b><i> Smart Parking as IOT Case Study: </i></b><br>

<img src="https://user-images.githubusercontent.com/87573003/126039428-6bd44120-1dfa-4b91-abeb-efa3281e0088.png" alt="Project Requirements" width="500"/>

<b><i> Team Members: </i></b><br>
- Aravind Maguluri [CS20MDS14011]
- Anurag Roy [CS20MDS14010]
- Bharat [CS20MDS14017]

<b><i> Smart Parking Overview: </i></b><br>

The increasing number of vehicles on road, along with the mismanagement of parking space, leads to parking-related problems; thankfully, smart parking systems offer solutions. Smart Parking has emerged as a key internet of things (IoT) use case that falls under the umbrella of smart city concept. Smart parking solutions help to reduce congestion and pollution as they eliminate the need for vehicles to circle looking for spaces.

<b><i>High level Design: </i></b> <br>

<img src="https://user-images.githubusercontent.com/87573003/126040245-6c99047d-da7d-4373-bcab-67de4f90329c.png" alt="High Level Design" width="1000"/>

<b><i>Components:</i></b><br>

Parking space sensor: 
- This is a ground based sensor emulated using software
- When a car is parked in a parking slot or taken out from a slot, the sensor sends notification to Gateway Server

Camera sensor: 
-  This is a camera that can take commands from the server and identify the location of car using OCR, this is emulated using software
-  When a request is recieved to find a car with reg. plate details, camera finds the slot it is parked if present

IOT Gateway Server: 
- This is a server/hub with HiveMQ and tinyDB
- HiveMQ acts as a platform for communication between server and sensors
- tinyDB is going to help us store the events in a miniature database for maintaining the state of the parking space

User Interface: 
- This is a simple command prompt that is available to the user to do the below queries
  -  List free parking slots
  - Given car 4 digits, list all slots with matching car details

<b><i>Communication between components:</i></b>
- Parking space sensor only sends one-way updates to the Gateway server on the MQTT topic - <b><u>smartparking/groundsensor/slot#</b></u>
- Gateway server requests camera sensor for parking slot of a car with reg. details - <b><u>smartparking/findcarbyplatedetails/request/</b></u>
- Camera Sensor sends the details of the parking slots of car given reg. details - <b><u>smartparking/findcarbyplatedetails/response/</b></u>
- User interface talks to the Gateway server to make requests
