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
import maths
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
	potential = my_hex.autos*2
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

def breakthrough(study_hex):
	if study_hex.av_coal < 100 and study_hex.h_type == "metro":
		# could not happen
		return False,study_hex

	study_hex.av_coal = study_hex.av_coal - 100
	return True,study_hex



