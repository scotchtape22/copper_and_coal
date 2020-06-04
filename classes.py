#!/bin/python
# Object Classes for Copper and Coal

import random

# Hex Object
class grid_hex:
  def __init__(self):
    # Grid ID
    self.grid_id = grid_id
    # Adjacent Grid IDs
    self.adjacencies = adjacencies
    # Settlement Name
    self.title = title
    # Resource Type
    self.type = type
    # Settlement is capital?
    self.capital = is_capital
    # Settlement infrastructure
    self.infra = infra
    # Automaton Counts (8 different Nations) stored as an array
    self.auto_count = auto_count
    #Calamity
    self.calamity = calamity
    
    def auto_growth(self)
    for x in auto_count:
      if x == 1:
        x = x + 1
      elif x >= 2:
        x = x + 2

# Nation Object
class nation:
  def __init__(self):
    # Reference ID
    # Player and token?
    # Terraform Score
    # Manufacture Bid
    # Airship Bid
    # Production Value
    # Copper
    # Coal
    # Barley
    # Automaton Count

# Map Object
# Contains all other objects
# Contains date
# Function List Based on Phases

# Move Function
# Takes in move order and 2 settlements
# Checks that move count is valid
# checks that adjacency is valid
# Performs move

# Other Functions
# Combat
  # Figure combat priority
  # Remove 
  
# Calamity Role
