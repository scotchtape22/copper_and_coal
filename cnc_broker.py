#!/bin/python


import pygame
import cnc_classes as cncc
import cnc_player as cncp
import map_maker as cnc_mm
from datetime import datetime

# Copper and Coal Broker

# Sits on the server, takes the map, loads it, sanitizes it based on the player's login information, and serves them the map.


###########
# Used internally by map loops
##########