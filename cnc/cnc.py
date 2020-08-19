#!/bin/python

# Copper and Coal Hex Testing

# Importing
import pygame

# Should import all the mechanical functions from a seperate file for simplicity
# Functions required for rendering map

# TODO: Debug Function


class some_hex():
	# Hex contains:
	# Position in game (cordinates)
	# Position on camera (position)
	# Owner
	# Automaton Count
	# Available Coal Count
	# Mineable Coal Count
	# Array of prisoners
	# Array of engineers
	# Array of war machines
	# Type of hex
	# Common name
	# Hex type file path
	def __init__(self,x,y):
		self.row = x 
		self.col = y
		# Used for cubic maths
		self.sss = -(x+y)

		# Used to work with camera/mouse
		self.pos_x = 0
		self.pos_y = 0
		self.hex_rect = pygame.Rect(0,0,0,0)

		self.selected = False


		# Load Hex Type Info Base on Hex Type
		self.bg_img_file = pygame.image.load('./hex_backdrops/hex_fort_empty.png')
		self.hex_rect = self.bg_img_file.get_rect()
		# Load Tile Stats

		# Other mathy things
		self.hex_width = self.bg_img_file.get_width()
		self.hex_height = self.bg_img_file.get_height()

		# Shrink image for now

def text_objects(text,font):
	textSurface = font.render(text, True, [0,0,0])
	return textSurface,textSurface.get_rect()

def draw_hex(my_hex):
	# Same x and y for things like selected hex, etc.
	c_x = my_hex.pos_x
	c_y = my_hex.pos_y

	# Draw the background
	gameDisplay.blit(my_hex.bg_img_file,[c_x,c_y])

	# Update rectangle
	my_hex.hex_rect = my_hex.bg_img_file.get_rect(topleft=[c_x,c_y])
	# Draw Control Color

	# If selected, draw hilighter
	if my_hex.selected == True:
		hilight = pygame.image.load('./hex_backdrops/hex_selected.png')
		gameDisplay.blit(hilight,[c_x,c_y])

	# Draw data based on info-level
	# 2 - all info, you own this hex
	# 1 - some info, in LoS
	# 0 - no info - not in LoS

	# If selected - draw popup for settlement based on info level

	# In the future will draw all hex variables, for now just the x/y values of the hex
	# Hex font 
	name_font=pygame.font.Font('freesansbold.ttf',12)
	auto_font=pygame.font.Font('freesansbold.ttf',18)
	coal_font=pygame.font.Font('freesansbold.ttf',18)

	# Debug - display cordinates (will eventually change to hex name)
	# Hexes are currently 96x96 so just hard code that for now, but if we ever want to zoom then we need to change this!
	cord_text = (str(my_hex.row)+"-"+str(my_hex.col))
	CordSurf,CordRect = text_objects(cord_text,name_font)
	CordRect.center = (c_x+48,(c_y+80))
	gameDisplay.blit(CordSurf,CordRect)


def push_map(map_array,direction):
	# Right is positive, left is negative
	# Move rectangles?
	for my_hex in map_array:
		my_hex.pos_x = my_hex.pos_x + direction


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
		# print(str(my_hex.row)+"-"+str(my_hex.col)+"=>"+str(this_x)+"-"+str(this_y))
		# If off screen, try and move?
		# draw_hex(my_hex)

def draw_map(map_array,row_d,disp_x):
	for my_hex in map_array:
		# Determine if on screen, it is is draw normally		
		# If not on screen, check if it can be moved?
		if 0 < my_hex.pos_x < disp_x:
			draw_hex(my_hex)
		else:
			# If beyond the right wall (max) and subtracting the row distance will put me above 0, subtract the row distance and draw!
			if my_hex.pos_x > disp_x and my_hex.pos_x - row_d > 0:
				my_hex.pos_x = my_hex.pos_x - row_d
				draw_hex(my_hex)
			# If beyond the left wall (0) and adding the row distance will put me below the display max, add the row distance and draw!
			elif my_hex.pos_x < 0 and my_hex.pos_x + row_d < disp_x:
				my_hex.pos_x = my_hex.pos_x + row_d
				draw_hex(my_hex)
			# If neither work, don't worry about drawing,

def select_hex(my_hex):
	my_hex.selected = True
	# Draw selection marker
	# Popup window of info/orders
	pass

def draw_toolbar(screen,disp_x):
	co_gold = [204,204,0]
	# Draw backdrop
	pygame.draw.rect(screen,co_gold,[0,0,disp_x,80])

	# Toolbar Font
	tool_font=pygame.font.Font('freesansbold.ttf',18)

	# Things on the toolbar
	# Intelligence Reports
	# Chat
	# File stuff
	# Calendar/Timer
	date_text = ("Spring - Year 1\nOrders Due: 15:00")

	dateSurf,dateRect = text_objects(date_text,tool_font)
	dateRect.center = (disp_x-100,15)
	gameDisplay.blit(dateSurf,dateRect)

	# Submit Orders button

def draw_hex_popup():
	pass
			

if __name__ == "__main__":
	pygame.init()


	# Display size should be the option
	display_width = 1280
	display_height = 800

	gameDisplay = pygame.display.set_mode([display_width,display_height])

	# Create a center we can work with
	orient_x = display_width/2
	orient_y = display_height/2

	# Maybe define a center?

	# Define Colors?
	co_black = [0,0,0]
	co_white = [255,255,255]
	co_red = [255,0,0]
	co_green = [0,255,0]
	co_blue = [0,0,255]
	co_bg = [175,195,125]
	# TODO - define in a style file

	# Game Window Title
	pygame.display.set_caption('Copper and Coal')

	# Set FPS Clock
	# Other clocks for order timing
	clock_1 = pygame.time.Clock()

	# Initialize junk

	# Exit Variable
	exited = False


	# TODO - Create starting map based on a load file
	# Define standard hex images
	# hex_example_image = pygame.image.load('./Hex_Example.png')
	# For now just make a bunch of hexes
	rows = 7
	columns = 16

	this_map = []

	while rows > 0:
		these_columns = columns
		while these_columns > 0:
			this_map.append(some_hex(these_columns,rows))
			these_columns = these_columns - 1
		rows = rows - 1

	# Calculate initial map position information:
	first_draw_map(this_map,orient_x,orient_y,display_width,display_height)

	# Calculate Row Distance for world warp
	row_d = columns*this_map[0].hex_width

##############################################
	# The UI Loop
	# Player Interactions with the game as well as showing the next orders

	# Get first window draw?

	while not exited:
		for event in pygame.event.get():
			# Exit Event
			if event.type == pygame.QUIT:
				# Prompt to submit orders if you have none
				exited = True
			if event.type == pygame.MOUSEBUTTONUP:
				# Check what was clicked - first, through the hexes
				x,y = event.pos
				if event.button == 1:
					# Left Click
					for my_hex in this_map:
						# Bange together an actual rect becasuse fuck it
						if my_hex.hex_rect.collidepoint(x,y):
							my_hex.selected = True
						else:
							my_hex.selected = False
					# If you didn't click a hex, you clicked a button?


				# Left - select a hex/option
				# Right - start a move

			# Every so often, will need to go new map state?
		#Check if Scrolling left/right - no need for up/down
		if pygame.mouse.get_pos()[0] < 10:
			push_map(this_map,15)
			# print("PUSH! left")
		elif pygame.mouse.get_pos()[0] > display_width - 10:
			push_map(this_map,-15)
			# print("PUSH! Right")

			# Potential Events
			# Select hex
			# Submit Orders
			# Chat
			# Replay last turn


		# Draw
		# 1 - Background, add dust clouds?
		gameDisplay.fill(co_bg)


		# 2 - Map
		draw_map(this_map,row_d,display_width)
		
		# 3 - Toolbar
		draw_toolbar(gameDisplay,display_width)

		# 4 - Queued Orders

		# 5 - Popups

		# 6 - Update 
		pygame.display.update()

		clock_1.tick(60)

	# Cleanup tasks
	pygame.quit()
	quit()

