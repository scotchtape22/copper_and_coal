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

def field_combat(army_1,army_2):
	# Army Array [Auto,Coal,Landships,Airships,Extractors,Devices,Components], maybe make this an object?
	# Returns the winning array
	cas_1 = 0
	cas_2 = 0

	# Landships cancel
	landship_balance = army_1.landships - army_2.landships

	while landship_balance != 0:
		if landship_balance > 0:
			if army_2.autos <= 10:
				army_2.autos = 0
				break
			else:
				army_2.autos = army_2.autos - 10
			landship_balance = landship_balance - 1
		elif landship_balance < 0:
			if army_1.autos <= 10:
				army_1.autos = 0
				break
			else:
				army_1.autos = army_1.autos - 10
			landship_balance = landship_balance + 1

	if army_1.autos > army_2.autos:
		# Army 1 wins
		army_1.autos = army_1.autos - army_2.autos
		return army_1
	elif army_1.autos < army_2.autos:
		army_2.autos = army_2.autos - army_1.autos
		return army_2
	else:
		return None


def siege_combat(army_1,tar_hex):
	# Army Array [Auto,Coal,Landships,Airships,Extractors,Devices,Components]
	# Returns the new hex

	# Defense
	# Defending automatons get a 
	if tar_hex.command == "defend":
		army_1.autos = army_1.autos - tar_hex.autos


	# If no automatons make it, everything is surrendered
	if army_1.autos < 1:
		# the target hax captures anything in the move
		tar_hex.av_coal = tar_hex.av_coal + army_1.coal
		while army_1.landships > 0:
			tar_hex.wm.append("landship")
			army_1.landships = army_1.landships - 1
		while army_1.airships > 0:
			tar_hex.wm.append("airship")
			army_1.airships = army_1.airships - 1
		while army_1.extractor > 0:
			tar_hex.wm.append("extractor")
			army_1.extractor = army_1.extractor - 1
		while army_1.devices > 0:
			tar_hex.wm.append("device")
			army_1.device = army_1.device - 1
		while army_1.components > 0:
			tar_hex.wm.append("component")
			army_1.component = army_1.component - 1
		return tar_hex

	# Landships battle
	landship_balance = army_1.landships - tar_hex.landships

	while landship_balance != 0:
		if landship_balance > 0:
			if tar_hex.autos <= 10:
				tar_hex.autos = 0
				break
			else:
				tar_hex.autos = tar_hex.autos - 10
			landship_balance = landship_balance - 1
		elif landship_balance < 0:
			if army_1.autos <= 10:
				army_1.autos = 0
				break
			else:
				army_1.autos = army_1.autos - 10
			landship_balance = landship_balance + 1

	# Game 
	balance = army_1.autos - tar_hex.autos:
	if balance > 0:
		# The hex is captured!
		tar_hex.controller = army_1.controller
		tar_hex.autos = tar_hex.autos + army_1.autos
		tar_hex.av_coal = tar_hex.av_coal + army_1.coal
		while army_1.landships > 0:
			tar_hex.wm.append("landship")
			army_1.landships = army_1.landships - 1
		while army_1.airships > 0:
			tar_hex.wm.append("airship")
			army_1.airships = army_1.airships - 1
		while army_1.extractor > 0:
			tar_hex.wm.append("extractor")
			army_1.extractor = army_1.extractor - 1
		while army_1.devices > 0:
			tar_hex.wm.append("device")
			army_1.device = army_1.device - 1
		while army_1.components > 0:
			tar_hex.wm.append("component")
			army_1.component = army_1.component - 1
		return tar_hex
	elif balance <= 0:
		# the target hax captures anything in the move
		tar_hex.av_coal = tar_hex.av_coal + army_1.coal
		while army_1.landships > 0:
			tar_hex.wm.append("landship")
			army_1.landships = army_1.landships - 1
		while army_1.airships > 0:
			tar_hex.wm.append("airship")
			army_1.airships = army_1.airships - 1
		while army_1.extractor > 0:
			tar_hex.wm.append("extractor")
			army_1.extractor = army_1.extractor - 1
		while army_1.devices > 0:
			tar_hex.wm.append("device")
			army_1.device = army_1.device - 1
		while army_1.components > 0:
			tar_hex.wm.append("component")
			army_1.component = army_1.component - 1
		return tar_hex


# Validate moves
def valid_moves(my_map,all_moves):
	# Returns a list of valid moves and the new map with the moves on their way
	valid_moves = []

	for my_hex in my_map:
		# Get a list of all the moves that match this
		hex_moves = []
		moving_autos = 0
		moving_coal = 0
		moving_landships = 0
		moving_airships = 0
		moving_devices = 0
		moving_extractors = 0
		moving_components = 0
		total_cost = 0
		for this_move in all_moves:
			if this_move.from_hex == my_hex:
				hex_moves.append(this_move)

		# Confirm that these moves can take 

# Sort Moves - assume all moves are valid
def sort_moves(my_map,all_moves):



