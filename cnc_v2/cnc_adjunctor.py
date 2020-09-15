#!/bin/python

# Server Side adjunctor for CNC
# Takes in:
# World, Nations, Map, Units, Orders
# Returns:
# World, Nations, Map, Units


# Imports
import pygame
# I don't actually think we need pygame, but I don't want to break this
import cnc_classes as cncc
import random
import datetime
import math
import map_maker as cnc_mm
import cnc_player as cncp

def produce(my_hex):
	# Takes in a hex and returns it with the new value of automatons

	if my_hex.type == "metro":
		my_hex.autos = my_hex.autos + (my_hex.autos/2) + 5
		my_hex.autos = math.ceil(my_hex.autos)
	else:
		my_hex.autos = my_hex.autos + (my_hex.autos/2)
		my_hex.autos = math.ceil(my_hex.autos)

	return my_hex


def auto_mine(my_hex):
	# Takes a hex and calculates the amount of coal produced
	extractor_pot = 0
	for mach in my_hex.wm:
		if mach == "extractor":
			extractor_pot = extractor_pot+25

	potential = (my_hex.autos*2)+extractor_pot
	if potential < my_hex.mine:
		my_hex.mine = my_hex.mine - potential
		my_hex.av_coal = my_hex.av_coal + potential
	else:
		# Just take the rest of the min
		my_hex.mine = 0
		my_hex.av_coal = my_hex.av_coal + my_hex.mine
	return my_hex

def bombed(my_hex):
	# Destroy a hex with an ejection
	# Drop all resources
	my_hex.materials = 0
	my_hex.av_coal = 0
	my_hex.autos = 0
	my_hex.mine = 0

	# Remove ownership
	my_hex.controller = None

	# Change type
	my_hex.h_type = "wastes"

	# Change rules
	my_hex.name = my_hex.name = " Ruins"

	return my_hex

def ejection(attack_hex,target_hex):
	# Need to determine if within 3
	# Return both hexes as well as a T/F if it was able to take place

	if attack_hex.av_coal < 50 and attack_hex.h_type == "metro":
		# could not happen
		return False,attack_hex,target_hex

	attack_hex.av_coal = attack_hex.av_coal - 50

	target_hex = bombed(target_hex)

	return True,attack_hex,target_hex

def component_build(study_hex):
	if study_hex.av_coal < 100 and study_hex.h_type == "metro":
		# could not happen
		return False,study_hex

	study_hex.av_coal = study_hex.av_coal - 100
	return True,study_hex

def supply(my_hex):
	total_cost = math.ceil(my_hex.autos/5)
	total_cost = total_cost + len(my_hex.wm)

	# Divide in half if the command was 
	if my_hex.command == "conserve":
		total_cost = math.ceil(total_cost/2)

	# Pay as much coal as you can
	if total_cost >= my_hex.av_coal:
		my_hex.av_coal = my_hex.av_coal - total_cost
		total_cost = 0
	else:
		total_cost = total_cost - my_hex.av_coal
		my_hex.av_coal = 0

	# Pay in autos then
	if total_cost == 0:
		return my_hex
	else:
		if total_cost >= my_hex.autos:
			my_hex.autos = my_hex.autos - total_cost
			total_cost = 0
		else:
			total_cost = total_cost - my_hex.autos
			my_hex.autos = 0

	if total_cost == 0:
		return my_hex

	# Pay in War Machines before
	for mach in my_hex.wm:
		if mach == "component":
			continue
		my_hex.wm.remove(mach)
		total_cost = total_cost - 1
		if total_cost == 0:
			return my_hex

	# Then remove components
	for mach in my_hex.wm:
		my_hex.wm.remove(mach)
		total_cost = total_cost - 1
		if total_cost == 0:
			return my_hex

	# If you still some how have anything, then just return what you have left
	return my_hex




