#!/bin/python


import pygame
import cnc_classes as cncc
import cnc_player as cncp
import map_maker as cnc_mm
from datetime import datetime

# Copper and Coal Player

# Being Actually on the map


###########
# Used internally by map loops
##########

def gamebar_buttons():

	button_icon = []
	button_icon.append(pygame.image.load('./images/icons/icon_menu.png'))
	button_icon.append(pygame.image.load('./images/icons/icon_intel.png'))
	button_icon.append(pygame.image.load('./images/icons/icon_mssg.png'))
	button_icon.append(pygame.image.load('./images/icons/icon_submit.png'))

	# Button Objects

	gb_buttons = []
	gb_buttons.append(cncc.a_button("","menu",None,None,[0,0,32,32],[0,0,0],[0,255,0],[255,0,0],[0,0,255],button_icon[0]))
	gb_buttons.append(cncc.a_button("","intel",None,None,[32,0,32,32],[0,0,0],[0,255,0],[255,0,0],[0,0,255],button_icon[1]))
	gb_buttons.append(cncc.a_button("","mssg",None,None,[64,0,32,32],[0,0,0],[0,255,0],[255,0,0],[0,0,255],button_icon[2]))
	gb_buttons.append(cncc.a_button("","submit",None,None,[96,0,32,32],[0,0,0],[0,255,0],[255,0,0],[0,0,255],button_icon[3]))

	return gb_buttons

def hex_buttons():
	button_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',18)
	button_color = cncc.get_color("inactive_button")
	text_color = cncc.get_color("inactive_text")
	button_prompt_color = cncc.get_color("active_button")
	text_prompt_color = cncc.get_color("active_text")

	unit_buttons = []
	unit_buttons.append(cncc.a_button("Support","support",None,button_font,[0,160,128,32],button_color,text_color,button_prompt_color,text_prompt_color))
	unit_buttons.append(cncc.a_button("Disband","disband",None,button_font,[128,160,128,32],button_color,text_color,button_prompt_color,text_prompt_color))
	return unit_buttons

def draw_gamebar(gamebar_buttons,screen,my_nation,my_world,display_width):
	# Draw toolbar
	# Get gamebar color
	gb_color = cncc.get_color("gamebar")
	gb_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',12)
	# Background
	pygame.draw.rect(screen, gb_color, [0,0,display_width,32])

	# Draw buttons
	for button in gamebar_buttons:
		button.draw(screen)

	# Draw World Info
	# Start from the far right

	# Time to next orders
	current_time = datetime.now()
	dueby_raw = my_world.due_date - current_time
	hours = dueby_raw.seconds // 3600
	minutes = dueby_raw.seconds // 60
	seconds = dueby_raw.seconds % 60
	due_by_readable = "%s:%s.%s" % (hours, minutes, seconds)

	# Draw date time
	cncc.draw_notice(screen,str(due_by_readable),gb_font,[display_width-128,0,128,32],gb_color,[0,0,0])

	# Draw season info
	# TODO: setup up weather icon
	# TODO: change to a previous season
	# TODO: prisoner menu
	# TODO: Rulebook menu
	# Just an empty 32 right now

	# Draw Year number, just a 32x32 square
	cncc.draw_notice(screen,str(my_world.year),gb_font,[display_width-192,0,32,32],gb_color,[0,0,0])

	# Season is a 64x32 - maybe needs to be made a 96?
	cncc.draw_notice(screen,str(my_world.season),gb_font,[display_width-256,0,64,32],gb_color,[0,0,0])



def queue_order(order_queue,new_order):
	# Takes in an order_queue and adds a new order to it, returning a new queue
	# Check internally that the order is valid
	# You have enough resources,
	# Check if the ordered unit/action exsists already - delete the old order

	# Add new order 
	if isinstance(new_order[0],cncc.map_hex):
		# Look to see if there is already of 
		for order in order_queue:
			if order[0] == new_order[0]:
				order_queue.remove(order)
				order_queue.append(new_order)
				return order_queue
	else:
		# Assume this is a move
		pass
	return order_queue

def banner_mode():
	# Print banner based on game state
	# Includes:
		# Testing
		# Map out of date
		# Game not yet started
	pass


def draw_orders(screen,order_queue,this_map,these_units):
	# Draw the orders too the screen
	pass

def push_map(map_array,direction):
	# Right is positive, left is negative

	# Move rectangles?
	if direction == "u":
		for my_hex in map_array:
			my_hex.pos_y = my_hex.pos_y + 30
	elif direction == "d":
		for my_hex in map_array:
			my_hex.pos_y = my_hex.pos_y - 30
	elif direction == "r":
		for my_hex in map_array:
			my_hex.pos_x = my_hex.pos_x + 30
	elif direction == "l":
		for my_hex in map_array:
			my_hex.pos_x = my_hex.pos_x - 30


def first_draw_map(map_array,cursor_x,cursor_y,disp_x,disp_y):

	# Calculate initial x positions for the map

	hex_width = map_array[0].hex_width
	hex_height = map_array[0].hex_height

	offset_horizontal = hex_width
	#offset_vertical = hex_height*0.75
	offset_vertical = hex_height

	# go through printing hexes
	for my_hex in map_array:
		# Draw calculate position and draw map at this 
		my_hex.pos_x = (offset_horizontal*(my_hex.row+(my_hex.col/2)))
		my_hex.pos_y = (offset_vertical*my_hex.col)

def draw_map(map_array,row_d,disp_x,hilight,screen,shadow):
	for my_hex in map_array:
		# If on screen, draw

		if 0 < my_hex.pos_x < disp_x:
			draw_hex(my_hex,screen,shadow)
		else:
		# If beyond the right wall (max) and subtracting the row distance will put me above 0, subtract the row distance and draw!
			if my_hex.pos_x > disp_x and my_hex.pos_x - row_d > 0:
				my_hex.pos_x = my_hex.pos_x - row_d
				draw_hex(my_hex,screen,shadow)
		# If beyond the left wall (0) and adding the row distance will put me below the display max, add the row distance and draw!
			elif my_hex.pos_x < 0 and my_hex.pos_x + row_d < disp_x:
				my_hex.pos_x = my_hex.pos_x + row_d
				draw_hex(my_hex,screen,shadow)

		# If neither work, don't worry about drawing,



def draw_hex(my_hex,gameDisplay,shadow):
	# Same x and y for things like selected hex, etc.
	c_x = my_hex.pos_x
	c_y = my_hex.pos_y

	# Draw the background
	gameDisplay.blit(my_hex.bg_img_file,[c_x,c_y])

	# Update rectangle
	my_hex.hex_rect = my_hex.bg_img_file.get_rect(topleft=[c_x,c_y])
	# Draw Control Color

	# Draw data based on info-level
	# 2 - all info, you own this hex
	# 1 - some info, in LoS
	# 0 - no info - not in LoS

	# If selected - draw popup for settlement based on info level

	# In the future will draw all hex variables, for now just the x/y values of the hex
	# Hex font 

	if my_hex.hex_type == "metro" or my_hex.hex_type == "mine":
		# If you are a sky hex, you are basically done
		name_font=pygame.font.Font('./fonts/steam_punk_flyer.ttf',12)
		# Draw hex name
		hex_name = my_hex.name
		NameSurf,NameRect = cncc.text_objects(hex_name,name_font)
		NameRect.center = ((((my_hex.pos_x*2)+my_hex.hex_width)/2),((((my_hex.pos_y)+my_hex.hex_height)-16)))
		gameDisplay.blit(NameSurf,NameRect)

		if my_hex.controller != None:
			gameDisplay.blit(my_hex.controller.sigil_img,[my_hex.pos_x+my_hex.hex_width-32,my_hex.pos_y])

		# Draw sigil for nation controlling this hex if it is controlled?
		# Need to figure out how to get the hex control from the nation


	# Data on the hex
	data_font=pygame.font.Font('./fonts/steam_punk_flyer.ttf',10)
	# Available coal and automatons is always presented, other info can be shown in the detail
	if my_hex.hex_type != "wastes":
		if my_hex.infolevel == 2:
			# Full Info (Our Hexes)
			# Automatons
			NameSurf,NameRect = cncc.text_objects(str(my_hex.autos),data_font)
			NameRect.center = (my_hex.pos_x+16,my_hex.pos_y+my_hex.hex_height-32)
			gameDisplay.blit(NameSurf,NameRect)
			# Automatons
			NameSurf,NameRect = cncc.text_objects(str(my_hex.av_coal),data_font)
			NameRect.center = (my_hex.pos_x+my_hex.hex_width-16,my_hex.pos_y+my_hex.hex_height-32)
			gameDisplay.blit(NameSurf,NameRect)
			# War Machines
			NameSurf,NameRect = cncc.text_objects(str(len(my_hex.wm)),data_font)
			NameRect.center = (my_hex.pos_x+16,my_hex.pos_y+my_hex.hex_height-64)
			gameDisplay.blit(NameSurf,NameRect)
		elif my_hex.infolevel == 1:
			# See total stuff
			total_stuff = my_hex.autos+my_hex.av_coal+(len(my_hex.wm)*25)
			NameSurf,NameRect = cncc.text_objects(str(total_stuff),data_font)
			NameRect.center = (my_hex.pos_x+16,my_hex.pos_y+my_hex.hex_height-32)
			gameDisplay.blit(NameSurf,NameRect)
		elif my_hex.infolevel == 0:
			gameDisplay.blit(shadow,[c_x,c_y])
	# See nothing from info level 0 hexes

	# If we add in engineers/war machines, maybe indicator lights showing these?

	# Debug - display cordinates (will eventually change to hex name)
	# Hexes are currently 96x96 so just hard code that for now, but if we ever want to zoom then we need to change this!
	# cord_text = (str(my_hex.row)+"-"+str(my_hex.col))
	# CordSurf,CordRect = cncc.text_objects(cord_text,name_font)
	# CordRect.center = (c_x+48,(c_y+80))
	# gameDisplay.blit(CordSurf,CordRect)

def make_hex_icons():
	# Return array of icons for hex buttons
	icon_array = []
	icon_array.append(pygame.image.load('./images/buttons/button-conserve.png'))
	icon_array.append(pygame.image.load('./images/buttons/button-defend.png'))
	icon_array.append(pygame.image.load('./images/buttons/button-mine.png'))
	icon_array.append(pygame.image.load('./images/buttons/button-autos.png'))
	icon_array.append(pygame.image.load('./images/buttons/button-landship.png'))
	icon_array.append(pygame.image.load('./images/buttons/button-airship.png'))

	return icon_array


def draw_hex_popup(screen,my_hex,hex_icons,my_nation):
	# Draw information on this hex
	insert_dem = [0,32,384,384]
	co_splash = [255,255,153]

	# Draw outside rectangle
	pygame.draw.rect(screen,co_splash,insert_dem)

	# Draw tile name
	title_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',24)
	detail_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',12)
	cncc.draw_notice(screen,my_hex.name,title_font,[0,64,300,30],co_splash,[0,0,0])

	if my_hex.controller != None:
		cncc.draw_notice(screen,my_hex.controller.playername,detail_font,[0,96,150,30],co_splash,[0,0,0])
	else:
		cncc.draw_notice(screen,"Free.",detail_font,[0,96,150,30],co_splash,[0,0,0])

	# Draw Tile Type
	if my_hex.hex_type == "metro":
		cncc.draw_notice(screen,"Metropolis",detail_font,[0,128,150,30],co_splash,[0,0,0])
	elif my_hex.hex_type == "mine":
		cncc.draw_notice(screen,"Mine",detail_font,[0,128,150,30],co_splash,[0,0,0])
	elif my_hex.hex_type == "wastes":
		cncc.draw_notice(screen,"Wasteland",detail_font,[0,128,150,30],co_splash,[0,0,0])
	elif my_hex.hex_type == "wilds":
		cncc.draw_notice(screen,"Wilderness",detail_font,[0,128,150,30],co_splash,[0,0,0])
	else:
		# Should only happen in error
		cncc.draw_notice(screen,"Unknown.",detail_font,[0,128,150,30],co_splash,[0,0,0])

	# Draw information based on available information level
	if my_hex.infolevel == 2:
		# See all detail in this hex
		cncc.draw_notice(screen,"Total Automatons:"+str(my_hex.autos),detail_font,[0,160,150,30],co_splash,[0,0,0])
		cncc.draw_notice(screen,"Available Coal:"+str(my_hex.av_coal),detail_font,[0,192,150,30],co_splash,[0,0,0])
		cncc.draw_notice(screen,"Coal Reserve:"+str(my_hex.mine),detail_font,[0,224,150,30],co_splash,[0,0,0])
		if my_hex.command == None:
			cncc.draw_notice(screen,"No directive for this quadrent yet.  Will conserve by default." ,detail_font,[0,192,150,30],co_splash,[0,0,0])
		else:
			cncc.draw_notice(screen,my_hex.command,detail_font,[0,192,150,30],co_splash,[0,0,0])
	elif my_hex.infolevel == 1:
		# See how much "stuff" is here
		cncc.draw_notice(screen,"Total Material:"+str(my_hex.material),detail_font,[0,160,150,30],co_splash,[0,0,0])
	elif my_hex.infolevel == 0:
		cncc.draw_notice(screen,"Quadrent too far",detail_font,[0,160,150,30],co_splash,[0,0,0])
		cncc.draw_notice(screen,"away to assess.",detail_font,[0,192,150,30],co_splash,[0,0,0])
	else:
		cncc.draw_notice(screen,"Quit cheating!",detail_font,[0,160,150,30],co_splash,[0,0,0])

	# Write the queued order if one exsists

	# Debug info level
	cncc.draw_notice(screen,"Info Level:"+str(my_hex.infolevel),detail_font,[0,256,150,30],co_splash,[0,0,0])
	cncc.draw_notice(screen,"Cordinates:"+str(my_hex.row)+":"+str(my_hex.col)+":"+str(my_hex.sss),detail_font,[0,288,150,30],co_splash,[0,0,0])


	context_menu = []

	if my_hex.hex_type == "wastes" or my_hex.controller != my_nation:
		# No buttons
		return context_menu
	else:
		context_menu.append(cncc.a_button("","conserve",my_hex,None,[256,64,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[0]))
		context_menu.append(cncc.a_button("","defend",my_hex,None,[320,64,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[1]))
		if my_hex.mine > 0:
			# If there is anything aviable, construct it
			context_menu.append(cncc.a_button("","extract",my_hex,None,[256,128,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[2]))
		else:
			# Just an empty button
			pass
		if my_hex.autos > 0:
			# If there is anything aviable, construct it
			context_menu.append(cncc.a_button("","build_autos",my_hex,None,[320,128,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[3]))
		else:
			# Just an empty button
			pass
		if my_hex.hex_type == "metro":
			if my_hex.av_coal >= 25:
				context_menu.append(cncc.a_button("","build_airship",my_hex,None,[256,192,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[4]))
				context_menu.append(cncc.a_button("","build_landship",my_hex,None,[320,192,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[5]))
				context_menu.append(cncc.a_button("","build_extractor",my_hex,None,[256,256,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[3]))
				context_menu.append(cncc.a_button("","build_device",my_hex,None,[320,256,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[3]))
			else:
				pass
			if my_hex.av_coal >= 100:
				context_menu.append(cncc.a_button("","build_component",my_hex,None,[288,320,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[3]))
			else:
				pass
			# Check if you have enough components 
			comp_count = 0
			for mech in my_hex.wm:
				if mech == "component":
					comp_count = comp_count + 1

			if comp_count >= 3 and my_hex.av_coal >= 200:
				context_menu.append(cncc.a_button("","launch",my_hex,None,[288,288,64,64],[0,0,0],[0,255,0],[255,0,0],[0,0,255],hex_icons[3]))
			else:
				pass
		return context_menu


# TODO: Def Update Map
# Update the map while the player is playing
def update_map():
	pass

def main_menu(screen):
	insert_dem = [0,32,128,160]
	co_splash = [255,255,153]


	button_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',16)
	mainmenu_buttons = []
	button_color = cncc.get_color("inactive_button")
	text_color = cncc.get_color("inactive_text")
	button_prompt_color = cncc.get_color("active_button")
	text_prompt_color = cncc.get_color("active_text")



	# Draw outside rectangle
	pygame.draw.rect(screen,co_splash,insert_dem)

	# Draw tile name

	mainmenu_buttons.append(cncc.a_button("Change Game","load",None,button_font,[0,64,128,32],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Options","opt",None,button_font,[0,96,128,32],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Quit","quit",None,button_font,[0,128,128,32],button_color,text_color,button_prompt_color,text_prompt_color))
	return mainmenu_buttons

	# Draws the menu, returns buttons in array

def move_context(hex_1,hex_2,my_map):
	insert_dem = [0,32,300,704]
	# Should change based on player count
	co_splash = [255,255,153]

	expected_cost = 0
	# TODO: Arrow Buttons

	# 

		


def intel_menu(screen,my_nation,all_nations):
	insert_dem = [0,32,300,704]
	# Should change based on player count
	co_splash = [255,255,153]

	# Button info:
	button_color = cncc.get_color("inactive_button")
	text_color = cncc.get_color("inactive_text")
	button_prompt_color = cncc.get_color("active_button")
	text_prompt_color = cncc.get_color("active_text")

	# Draw outside rectangle
	pygame.draw.rect(screen,co_splash,insert_dem)
	menu_buttons = []

	# Draw tile name
	title_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',24)
	detail_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',12)
	cncc.draw_notice(screen,"Intelligence Report",title_font,[0,64,300,30],co_splash,[0,0,0])

	# Your nations status
	cncc.draw_notice(screen,"My Components:"+str(my_nation.score),detail_font,[0,128,300,30],co_splash,[0,0,0])
	cncc.draw_notice(screen,"Spies Available",detail_font,[0,160,300,30],co_splash,[0,0,0])

	cursor_x = 192
	# All other nations
	for this_nation in all_nations:
		# No need to draw your own nation
		if this_nation.playername == my_nation.playername:
			continue
		cncc.draw_notice(screen,this_nation.playername+" Components:"+str(this_nation.score),detail_font,[0,cursor_x,300,30],co_splash,[0,0,0])
		cursor_x = cursor_x+32
		menu_buttons.append(cncc.a_button("Coup","coup",this_nation,detail_font,[0,cursor_x,99,30],button_color,text_color,button_prompt_color,text_prompt_color))
		menu_buttons.append(cncc.a_button("Observe","observe",this_nation,detail_font,[100,cursor_x,99,30],button_color,text_color,button_prompt_color,text_prompt_color))
		menu_buttons.append(cncc.a_button("Counter","counter",this_nation,detail_font,[200,cursor_x,99,30],button_color,text_color,button_prompt_color,text_prompt_color))
		cursor_x = cursor_x+32

	# print(cursor_x)
	# cncc.draw_notice(screen,"Reset Spies",detail_font,[0,cursor_x,300,30],co_splash,[0,0,0])
	menu_buttons.append(cncc.a_button("Reset Spies","spy_reset",None,detail_font,[0,cursor_x,300,30],button_color,text_color,button_prompt_color,text_prompt_color))

	return menu_buttons

def mssg_menu():
	pass

def const_menu():
	pass
	# Menu construction
	
#############
# The 2 calls that should be coming from outside the game
#############

def test_map():
	# A test of running the map

	pygame.init()


	# Display size should be the option
	display_width = 1280
	display_height = 800

	gameDisplay = pygame.display.set_mode([display_width,display_height])

	nations,this_map,my_world,row_d = cnc_mm.quick_map()

	my_nation = nations[0]

	# Create Images So we don't have to worry about it later
	hilight = pygame.image.load('./images/hexes/hex_select.png')
	shadow = pygame.image.load('./images/hexes/shadow.png')
	target = pygame.image.load('./images/hexes/hex_target.png')

	# Toolbar Icons


	# TODO - grab the actual number of columns, will need to figure out how to grab from the map
	
	# TODO - Load buttons

	# Define FPS Clock
	clock_1 = pygame.time.Clock()


	# Get buttons for the icons for game bar
	gb_buttons = gamebar_buttons()
	hex_buttons = make_hex_icons()

	# Set initial click variable
	click_select = None
	insta_select = None
	context_menu = []

	local_order_queue = []
	# TODO: Figure out a way to load your orders

	# first_draw_map
	first_draw_map(this_map,0,0,display_width,display_height)

	# Get fog or war
	# Will need to run this when the map updates
	this_map = cncc.fog_o_war(this_map,my_nation,row_d)

	# Begin the loop!
	playing = True

	while playing:
		# Check if map needs updating
		for event in pygame.event.get():
			# Exit Event
			if event.type == pygame.QUIT:
				# Prompt to submit orders if you have none
				cncc.game_quit()
				exited = True
			if event.type == pygame.MOUSEBUTTONUP:
				# Check what was clicked - first, through the hexes
				x,y = event.pos
				print(event.button)
				if event.button == 1:
					# Left Click - only click
					nada = True
					# Toolbar Button
					for my_button in gb_buttons:
						if my_button.but_rect.collidepoint(x,y):
							# print(my_button.button_id)
							if my_button.button_id == "submit":
								print(local_order_queue)
							click_select = my_button
							nada = False
					# 		my_button.function
					if nada == False:
						break
					# Context button
					for my_button in context_menu:
						if my_button.but_rect.collidepoint(x,y):
							# This should almost always be an instant change instead of a selection change you can't
							#print(my_button.button_id)
							# Buttons for this hex (assume click_select == map_hex), may want to confirm this
							if my_button.button_id == "conserve":
								click_select.command == "Conservation Initiative"
								queue_order(local_order_queue,[click_select,"conserve"])
							elif my_button.button_id == "defend":
								click_select.command == "Defense Initative"
								queue_order(local_order_queue,[click_select,"defend"])
							elif my_button.button_id == "extract":
								click_select.command == "Extract Coal"
								queue_order(local_order_queue,[click_select,"extract"])
							elif my_button.button_id == "build_autos":
								click_select.command == "Build Automatons"
								queue_order(local_order_queue,[click_select,"build_autos"])
							elif my_button.button_id == "build_airship":
								click_select.command == "Build Airship"
								queue_order(local_order_queue,[click_select,"build_airship"])
							elif my_button.button_id == "build_landship":
								click_select.command == "Build Landship"
								queue_order(local_order_queue,[click_select,"build_landship"])
							elif my_button.button_id == "build_extractor":
								click_select.command == "Build Extractor"
								queue_order(local_order_queue,[click_select,"build_extractor"])
							elif my_button.button_id == "build_device":
								click_select.command == "Build Doomsday Device"
								queue_order(local_order_queue,[click_select,"build_device"])
							elif my_button.button_id == "build_component":
								click_select.command == "Build City Component"
								queue_order(local_order_queue,[click_select,"build_component"])
							elif my_button.button_id == "launch":
								click_select.command == "Launching City"
								queue_order(local_order_queue,[click_select,"Launch"])

							# Agent Actions



							# Generally shouldn't change the click select
							nada = False
					# 		my_button.function
					if nada == False:
						break									
					for my_hex in this_map:
						# Bange together an actual rect becasuse fuck it
						if my_hex.hex_rect.collidepoint(x,y):
							my_hex.selected = True
							click_select = my_hex
							nada = False
						else:
							my_hex.selected = False
					if nada == False:
						break	
						# If a hex was selected, check if there is a unit to select too?
					# If nothing was selected, back up?
					if nada:
						click_select = None
						context_menu = []




					# If you didn't click a hex, you clicked a button?
					# If you clicked nothing
				elif event.button == 3 and isinstance(click_select,cncc.my_hex):
					print("Move!")

				# Left - select a hex/option
				# Right - start a move

			# Every so often, will need to go new map state?
		#Check if Scrolling left/right - no need for up/down
		if pygame.mouse.get_pos()[0] < 30:
			push_map(this_map,"r")
		elif pygame.mouse.get_pos()[0] > display_width - 30:
			push_map(this_map,"l")

		# Push up and down
		if 30 < pygame.mouse.get_pos()[1] < 60:
			push_map(this_map,"u")
		elif pygame.mouse.get_pos()[1] > display_height - 30:
			push_map(this_map,"d")


		# Draw
		# 1 - Background - Orange
		gameDisplay.fill(cncc.get_color("bg"))


		# 2 - Map and Units
		draw_map(this_map,row_d,display_width,hilight,gameDisplay,shadow)



		# Hilight the appropriate hex
		# Done in a different hex in order to not draw over other hexes
		if click_select:
			if isinstance(click_select,cncc.map_hex):
				# Hilight selected hex
				gameDisplay.blit(hilight,[click_select.pos_x,click_select.pos_y])
				# If this is your hex, show range
				if click_select.controller == my_nation:
					if "airship" in click_select.wm:
						# If you have an airship can target up to 2 spaces away
						for my_hex in this_map:
							if cncc.range_two(click_select,my_hex,row_d):
								gameDisplay.blit(target,[my_hex.pos_x,my_hex.pos_y])
					else: 
						# Just adjaceny
						for my_hex in this_map:
							if cncc.is_adjacent(click_select,my_hex,row_d):
								gameDisplay.blit(target,[my_hex.pos_x,my_hex.pos_y])


		# 4 - If you have a that has potential targets?

		# 4 - Toolbar
		# May need to define an array of buttons out here so that they can be clicked
		draw_gamebar(gb_buttons,gameDisplay,my_nation,my_world,display_width)

		# 4 - Queued Orders

		# 5 - Popups
		# Draw popup of the selected hex
		# Maybe have a selector that changes based on the last click?
		if click_select:
			if isinstance(click_select,cncc.map_hex):
				# OR IF A BUTTON WITHIN THE HEX POPUP IS CLICKED!
				context_menu = draw_hex_popup(gameDisplay,click_select,hex_buttons,my_nation)
				# Hilight selected hex
				gameDisplay.blit(hilight,[click_select.pos_x,click_select.pos_y])
			elif isinstance(click_select,cncc.a_button):
				if click_select.button_id == "menu":
					context_menu = main_menu(gameDisplay)
				elif click_select.button_id == "intel":
					context_menu = intel_menu(gameDisplay,my_nation,nations)
				elif click_select.button_id == "mssg":
					pass

				# Button Functions go here?

		# 6 - Draw buttons from click select
		for button in context_menu:
			button.draw(gameDisplay)

		# 7 - Update 
		pygame.display.update()

		clock_1.tick(90)

	# Cleanup tasks
	pygame.quit()
	quit()





def load_map():
	pass