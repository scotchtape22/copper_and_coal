#!/bin/python

# CNC Hex Testing

# Importing
import pygame
import os

# Should import all the mechanical functions from a seperate file for simplicity
# Functions required for rendering map

# TODO: Debug Function


class some_hex():
	def __init__(self,x,y,h_type):
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
		self.hex_type = h_type

		if self.hex_type == "field":
			self.bg_img_file = pygame.image.load('./images/hex_files/field_1.png')
			self.name = "Wildnerness"
			self.controller = "Un Owned"
		elif self.hex_type == "wizard":
			self.bg_img_file = pygame.image.load('./images/hex_files/wizard-tower.png')
			self.name = "Wizard Tower"
			self.controller = "The High Court"
		elif self.hex_type == "hamlet":
			self.bg_img_file = pygame.image.load('./images/hex_files/hamlet_1.png')
			self.name = "A Hamlet"
			self.controller = "Some House"

		self.hex_rect = self.bg_img_file.get_rect()
		
		# Load Tile Stats

		# Tile info level based on ownership - used to define
		self.infolevel = 2

		# Other mathy things
		self.hex_width = self.bg_img_file.get_width()
		self.hex_height = self.bg_img_file.get_height()

		# Shrink image for now

class a_button:
	# Initilization 
	# Draw function
	# Button Identifier - lets you perform a function based on button presses
	def __init__(self,message,button_id,font,button_dem,sq_co=[255,255,255],tx_co=[0,0,0],sq_p_co=[255,255,255],tx_p_co=[0,0,0],img_file=None):
		
		self.message = message
		self.button_id = button_id
		self.font = font
		self.button_dem = button_dem
		self.sq_co = sq_co
		self.tx_co = tx_co
		self.sq_p_co = sq_p_co
		self.tx_p_co = tx_p_co
		self.but_rect = pygame.Rect(button_dem)

		if img_file:
			self.img_fl = pygame.image.load(img_file)
		else:
			img_fl = None

	def draw(self):
		mouse = pygame.mouse.get_pos()
		# Get mouse position real quick to see if this is highlighted
		if self.img_fl:
			# If image, assume that the image has the text
			gameDisplay.blit(self.img_fl,[self.button_dem[0],self.button_dem[1]])
			if self.but_rect.collidepoint(mouse):
				# If this is the case, draw a transparent rectangle around the button
				pygame.draw.rect(gameDisplay, [0,0,0], self.button_dem


		# Else, draw rectangle

class world():
	# World data,calender, totals of wizards
	def __init__(self,season,year,total_wiz):
		self.season = season
		self.year = year
		self.total_wiz = total_wiz

class heirs():
	pass

class units():
	def __init__():
		pass

	pass

class your_house():
	# House of the player who is viewing the map - information is loaded from save
	def __init__(self):
		# Information for this house - all informatin
		if god == True:
			# If god is selected, player is in observer mode
			pass

		# Get House Sigil
		self.sigil_img = pygame.image.load('')

		# Get Resource Counts
		self.my_auth = auth
		self.my_mp = mp
		self.my_wz = wiz

		# Get scoring position (ie: how many players are ahead of you)
		self.position = position

class enemy_house():
	pass


def game_quit():
	# Play quit sound
	pygme.quit()
	quit()

def load_game(load_file,house):
	pass
	# Loads a game from a file and perspective

def text_objects(text,font,color=[0,0,0]):
	textSurface = font.render(text, True, color)
	return textSurface,textSurface.get_rect()

def draw_hex(my_hex,hilighter):
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
		gameDisplay.blit(hilighter,[c_x,c_y])

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
		# print(str(my_hex.row)+"-"+str(my_hex.col)+"=>"+str(this_x)+"-"+str(this_y))
		# If off screen, try and move?
		# draw_hex(my_hex)

def draw_notice(message,font,button_dem,sq_co=[255,255,255],tx_co=[0,0,0],img_fl=None):
	# Draw a basic message box, that provides only indication
	# Message = String to be written
	# Font = Font type, pygame.font.Font object
	# button_dem = Rectangle Array [x,y,w,h]
	# SQ = Square Color
	# TX = Text color
	# img_fl = file for if this should be an image = IMAGE - not filepath

	if img_fl:
		gameDisplay.blit(img_fl,[button_dem[0],button_dem[1]])
		return
		# If an image is highted, shade it
	else:
		button_x_center = ((button_dem[0]*2)+button_dem[2])/2
		button_y_center = ((button_dem[1]*2)+button_dem[3])/2
		pygame.draw.rect(gameDisplay, sq_co, button_dem)
		button_surf, text_rect = text_objects(message,font,tx_co)
		# Draw Text
		text_rect.center = (button_x_center,button_y_center)
		gameDisplay.blit(button_surf,text_rect)
	

def draw_map(map_array,row_d,disp_x,hilight):
	for my_hex in map_array:
		# Determine if on screen, it is is draw normally		
		# If not on screen, check if it can be moved?
		draw_hex(my_hex,hilight)


		# No screen wrap in this game
		# if 0 < my_hex.pos_x < disp_x:
		# 	draw_hex(my_hex)
				
		# else:
		# 	# If beyond the right wall (max) and subtracting the row distance will put me above 0, subtract the row distance and draw!
		# 	if my_hex.pos_x > disp_x and my_hex.pos_x - row_d > 0:
		# 		my_hex.pos_x = my_hex.pos_x - row_d
		# 		draw_hex(my_hex)
		# 	# If beyond the left wall (0) and adding the row distance will put me below the display max, add the row distance and draw!
		# 	elif my_hex.pos_x < 0 and my_hex.pos_x + row_d < disp_x:
		# 		my_hex.pos_x = my_hex.pos_x + row_d
		# 		draw_hex(my_hex)
			# If neither work, don't worry about drawing,

def select_hex(my_hex):
	my_hex.selected = True
	# Draw selection marker
	# Popup window of info/orders

def map_loop():
	# This is where the actual game goes once we have menus working
	pass

def make_tool_buttons():
	# Defines all buttons on the toolbar and returns them as an array of object
	button_font = pygame.font.Font('freesansbold.ttf',12)
	toolbar_buttons = []
	toolbar_buttons.append(a_button("menu","menu",button_font,[0,0,32,32],[255,255,255],[0,0,0],[255,255,255],[0,0,0],'./images/icons/menu.png'))
	toolbar_buttons.append(a_button("wiz","wiz",button_font,[160,0,32,32],[255,255,255],[0,0,0],[255,255,255],[0,0,0],'./images/icons/wizard.png'))
	toolbar_buttons.append(a_button("mssg","mssg",button_font,[224,0,32,32],[255,255,255],[0,0,0],[255,255,255],[0,0,0],'./images/icons/mssg.png'))
	toolbar_buttons.append(a_button("submit_no","submit_no",button_font,[256,0,32,32],[255,255,255],[0,0,0],[255,255,255],[0,0,0],'./images/icons/submit_no.png'))
	# Marriages
	return toolbar_buttons



def draw_toolbar(screen,disp_x,buttons,img_icons,this_world):
	co_gold = [204,204,0]
	# Draw backdrop
	pygame.draw.rect(screen,co_gold,[0,0,disp_x,32])

	# Toolbar Font
	tool_font=pygame.font.Font('freesansbold.ttf',18)

	# Things on the toolbar
	# Resources:
		# Authority (image 0)
		# Manpower Available (image 1)
		# Info Buttons are all in 
			# Wizards
			# Marriages
			# Messages
			# Submits
			# Menu
	# Calendar/Timer
		# Need to bring in game data
	date_text = this_world.season+", Year "+this_world.year
	tomove_text = ("Orders Due: 15:00")
	my_auth = "0"
	auth_img = img_icons[0]
	my_mp = "0"
	mp_img = img_icons[1]
	my_wz = "0"


	# Menu button is at 0
	draw_notice("",tool_font,[32,0,30,30],co_gold,[0,0,0],auth_img)
	draw_notice(my_auth,tool_font,[64,0,30,30],co_gold,[0,0,0])
	draw_notice("",tool_font,[96,0,30,30],co_gold,[0,0,0],mp_img)
	draw_notice(my_mp,tool_font,[128,0,30,30],co_gold,[0,0,0])
	# Wizard Icon (Button) should be at 160
	draw_notice(my_wz,tool_font,[192,0,30,30],co_gold,[0,0,0])
	# MSSG Button at 224
	# Submit Button is at 256

	draw_notice(date_text,tool_font,[disp_x-128,0,30,30],co_gold,[0,0,0])
	draw_notice(tomove_text,tool_font,[disp_x-320,0,30,30],co_gold,[0,0,0])

	# Draw buttons - see make_tool_buttons for thier information
	for button in buttons:
		button.draw()

	# Submit Orders button

def draw_hex_popup(screen,my_hex):
	# Draw information on this hex
	insert_dem = [0,32,300,200]
	co_splash = [255,255,153]

	# Draw outside rectangle
	pygame.draw.rect(screen,co_splash,insert_dem)

	# Draw tile name in a notce?
	title_font = pygame.font.Font('freesansbold.ttf',18)
	draw_notice(my_hex.name,title_font,[0,64,300,30],co_splash,[0,0,0])
	draw_notice(my_hex.controller,title_font,[0,96,150,30],co_splash,[0,0,0])




	# Draw potential actions and authority spending?
	

			

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
	co_bg = [0,153,255]
	# TODO - define in a style file

	# Game Window Title
	pygame.display.set_caption('Scepters, Knives, and Wands')

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

	# This stuf should Ideally all be loaded from a file
	this_map = []
	this_world = world("Summer","1","10")
	these_units = []
	these_heirs = []

	# These can be set now because they shouldn't change location
	# Array of dimensions and a name?
	my_tool_buttons = make_tool_buttons()
	print(my_tool_buttons)

	# Tile buttons may change based on options avaiable for the current selection, so just leave this blank for now
	my_tile_buttons = []


	# For now just make a map
	rows = 7
	columns = 16

	while rows > 0:
		these_columns = columns
		while these_columns > 0:
			if rows == 5 and these_columns == 8:
				this_map.append(some_hex(these_columns,rows,"wizard"))
			elif rows == 3 and these_columns == 9:
				this_map.append(some_hex(these_columns,rows,"hamlet"))
			else:
				this_map.append(some_hex(these_columns,rows,"field"))
			these_columns = these_columns - 1
		rows = rows - 1

	# Calculate initial map position information:
	first_draw_map(this_map,orient_x,orient_y,display_width,display_height)

	# Other standard bits of info we haven't placed yet
	hilight = pygame.image.load('./images/hex_files/hex_selected.png')
	img_icons = [pygame.image.load('./images/icons/authority.png'),
		pygame.image.load('./images/icons/man_power.png')]
	click_select = None

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
				game_quit()
				exited = True
			if event.type == pygame.MOUSEBUTTONUP:
				# Check what was clicked - first, through the hexes
				x,y = event.pos
				if event.button == 1:
					# Left Click
					nada = True
					# Check if it was a hex
					for my_hex in this_map:
						# In the winter, only select hexes, in campaign seasons, select units
						# Bange together an actual rect becasuse fuck it
						if my_hex.hex_rect.collidepoint(x,y):
							my_hex.selected = True
							click_select = my_hex
							nada = False
						else:
							my_hex.selected = False
					for my_button in my_tool_buttons:
						if my_button.but_rect.collidepoint(x,y):
							print(my_button.button_id)
							click_select = my_button
							nada = False
					# 		my_button.function
					#		

					# If nothing was selected, back up?
					if nada:
						click_select = None



					# If you didn't click a hex, you clicked a button?
					# If you clicked nothing


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
		# 1 - Background - Ocean
		gameDisplay.fill(co_bg)


		# 2 - Map and Units
		draw_map(this_map,row_d,display_width,hilight)
		#draw_units(these_units,this_map)

		# 3 - Toolbar
		# May need to define an array of buttons out here so that they can be clicked
		draw_toolbar(gameDisplay,display_width,my_tool_buttons,img_icons,this_world)

		# 4 - Queued Orders

		# 5 - Popups
		# Draw popup of the selected hex
		# Maybe have a selector that changes based on the last click?
		if click_select:
			if isinstance(click_select,some_hex):
				# OR IF A BUTTON WITHIN THE HEX POPUP IS CLICKED!
				draw_hex_popup(gameDisplay,click_select)
			elif isinstance(click_select,a_button):

				pass
				# Button Functions go here?


		# 6 - Update 
		pygame.display.update()

		clock_1.tick(90)

	# Cleanup tasks
	pygame.quit()
	quit()

