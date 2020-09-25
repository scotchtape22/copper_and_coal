#!/bin/python

# Imports
import cnc_classes as cncc
import socket

serv_sock = socket.socket()

# Loop to listen for answers

# Recieved Packets Are JSONs with:
# # Authentication
# # Game ID
# # Packet Type -
# # # Login
# # # List of games this player is in
# # # Joining a game
# # # Creating a game
# # # Submit Orders
# # # Load a game
# # # Send Message
# # Packet Data

# Packets sent
# New map
# Messages

# Queue messages and them send them when a player is logged in
while True:
	pass