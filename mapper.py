#!/bin/python

# Hex object

# 

def __make_map__(options):
	# Requiers a dictionary of information
	# Returns a map and game settings as an object

	# Set information from dictionary:
	game_speed = options['g_speed']
	day_skip = options['d_skip']
	colony_limit = options['c_limit']
	comm_type = options['c_type']
	

	

	
	
	# Create hexes based on player count
	# Determine limits for neutral cities
	# 4,6,8 players
	
	n_ports = 0
	n_purifiers = 0
	n_foundaries = 0
	y_limit = 0
	
	if options['p_count'] == 4:
	elif options['p_count'] == 6:
	elif options['p_count'] == 8:
	else:
		error("Invalid player count.")

	# Create empty grid
	y = 0
	y_now = 0
	x = 0
	
	while y_now < y_limit:
	


	# Create prime hex
	# Always Elysium port

	# Create player home bases
	if options['p_count'] == 4:
	elif options['p_count'] == 6:
	elif options['p_count'] == 8:
	else:
		error("Invalid player count.")
	
	
	# Fill neutrals
	# Ports first
	while n_ports > 0:
		# Pick spot
		
	# Then Purifiers
	# Then Foundaries
	
	# Build object
	
