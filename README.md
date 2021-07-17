<h1> Smart Parking - IOT Project </h1>

<b><i> Team Members: </i></b><br>
- Aravind Maguluri [CS20MDS14011]
- Anurag Roy [CS20MDS14010]
- Bharat [CS20MDS14017]

<b><i> Smart Parking Overview: </i></b><br>

The increasing number of vehicles on road, along with the mismanagement of parking space, leads to parking-related problems; thankfully, smart parking systems offer solutions. Smart Parking has emerged as a key internet of things (IoT) use case that falls under the umbrella of smart city concept. Smart parking solutions help to reduce congestion and pollution as they eliminate the need for vehicles to circle looking for spaces.

<b><i> Smart Parking as IOT Case Study: </i></b><br>

<img src="https://user-images.githubusercontent.com/87573003/126039428-6bd44120-1dfa-4b91-abeb-efa3281e0088.png" alt="Project Requirements" width="500"/>

<b> High level Design: </b> <br>



Parking space sensor: Send updates to MQTT topic for arrival and departure, one topic per sensor. Topic could be of the format - “smartparking/groundsensor/slot#”.

Camera sensor: Find car given reg. plate details, no other functionality required.

IOT Gateway Server: This is a server with HiveMQ and tinyDB. HiveMQ will provide a platform for communication between server and sensors. tinyDB is going to help us store the events in a miniature database for maintaining the state of the parking space.

User Interface: This is a simple command prompt that is available to the user to do the below queries
List free parking slots
Given car 4 digits, list all slots with matching car details

Communication between components:

Parking space sensor only sends one-way updates to the Gateway server
Gateway server requests the camera sensor for the parking slot of a car given reg. details
User interface talks to the Gateway server to make requests
