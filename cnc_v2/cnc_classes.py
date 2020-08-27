#!/bin/bash


import pygame

class map_hex():
	def __init__(self,x,y,h_type,player,name,automatons,available,mine):
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

		if self.hex_type == "wilds":
			self.bg_img_file = pygame.image.load('./images/hexes/wilds.png')
		elif self.hex_type == "mine":
			self.bg_img_file = pygame.image.load('./images/hexes/mine.png')
		elif self.hex_type == "metro":
			self.bg_img_file = pygame.image.load('./images/hexes/metro.png')
		elif self.hex_type == "wastes":
			self.bg_img_file = pygame.image.load('./images/hexes/wastes.png')
		else:
			# Error out
			return

		self.name = name
		self.controller = player

		self.hex_rect = self.bg_img_file.get_rect()
		
		# Load Tile Stats
		self.autos = automatons
		self.av_coal = available
		self.mine = mine
		self.material = automatons+available

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
			self.img_fl = img_file
		else:
			self.img_fl = None

	def draw(self,screen):
		mouse = pygame.mouse.get_pos()
		# Get mouse position real quick to see if this is highlighted
		if self.img_fl:
			# If image, assume that the image has the text
			screen.blit(self.img_fl,[self.button_dem[0],self.button_dem[1]])
			if self.but_rect.collidepoint(mouse):
				# If this is the case, draw a transparent rectangle around the button
				pygame.draw.rect(screen, [0,0,0], self.button_dem)
		else:
			button_x_center = ((self.button_dem[0]*2)+self.button_dem[2])/2
			button_y_center = ((self.button_dem[1]*2)+self.button_dem[3])/2
			if self.but_rect.collidepoint(mouse):
				# If on this, use the prompt colors
				pygame.draw.rect(screen, self.sq_p_co, self.button_dem)
				button_surf, text_rect = text_objects(self.message,self.font,self.tx_p_co)
			else:
				pygame.draw.rect(screen, self.sq_co, self.button_dem)
				button_surf, text_rect = text_objects(self.message,self.font,self.tx_co)
			# Draw text
			text_rect.center = (button_x_center,button_y_center)
			screen.blit(button_surf,text_rect)


		# Else, draw rectangle
def draw_notice(gameDisplay,message,font,button_dem,sq_co=[255,255,255],tx_co=[0,0,0],img_fl=None):
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
		pygame.draw.rect(gameDisplay, sq_co, button_dem)
		if font:
			button_x_center = ((button_dem[0]*2)+button_dem[2])/2
			button_y_center = ((button_dem[1]*2)+button_dem[3])/2
			button_surf, text_rect = text_objects(message,font,tx_co)
			# Draw Text
			text_rect.center = (button_x_center,button_y_center)
			gameDisplay.blit(button_surf,text_rect)

class world():
	# World data,calender, totals of wizards
	def __init__(self,season,year,weather,due_date):
		self.season = season
		self.year = year
		self.weather = weather

		self.due_date = due_date

		self.score = 3
		# Load weather icons here?
		# Needs the next due date as well for orders

	def weather_icon(self):
		pass
		# Use weather term to choose icon to load

class init_order():
	# Tile orders
	pass

class move_order():
	# Move orders
	pass

class your_nation():
	# House of the player who is viewing the map - information is loaded from save
	def __init__(self,playername,sigil_fp,color,god,colonies):


		# Get House Sigil as object, may need to change to fp
		self.sigil_img = pygame.image.load(sigil_fp)

		self.playername = playername
		#Also may want to pass a token of proof?

		# Color array
		self.nat_color = color

		# If god is selected, player is in observer mode

		self.god = god

		self.score = colonies

		# Need a symbol



class enemy_nation():
	pass

def text_objects(text,font,color=[0,0,0]):
	textSurface = font.render(text, True, color)
	return textSurface,textSurface.get_rect()

def get_color(color):
	# Returns an RGB array
	if color == "bg":
		return [255,217,179]
	elif color == "inactive_button":
		return [204,153,0]
	elif color == "active_button":
		return [153,102,51]
	elif color == "inactive_text":
		return [255,255,179] 
	elif color == "active_text":
		return [230,230,0]
	elif color == "gamebar":
		return [255,255,204]
	elif color == "white":
		return [255,255,255]
	elif color == "black":
		return [0,0,0]
	else:
		return [0,255,0]
	# Else should return lime green to show an error

def fog_o_war(this_map,my_nation):
	# Returns a new map with the appropriate information levels
	# Only run after orders occur
	my_hexes = []
	
	# Assume you know nothing except for what you see
	for my_hex in this_map:
		if my_hex.controller == my_nation:
			my_hex.infolevel = 2
			my_hexes.append(my_hex)
		else:
			my_hex.infolevel = 0

	# Go through Looking for hexes adjacent to your own
	for other_hex in this_map:
		if other_hex.controller == my_nation:
			other_hex.infolevel = 2
			continue
		else:
			for near_hex in my_hexes:
				if is_adjacent(near_hex,other_hex):
					other_hex.infolevel = 1
					break

	return this_map


def is_adjacent(hex_1,hex_2):
	# Returns True or Fase depending on if 2 hexes are adjacent
	if hex_1.row+1 == hex_2.row and hex_1.col -1 == hex_2.col and hex_1.sss == hex_2.sss:
		return True
	elif hex_1.row+1 == hex_2.row and hex_1.col == hex_2.col and hex_1.sss-1 == hex_2.sss:
		return True
	elif hex_1.row == hex_2.row and hex_1.col+1 == hex_2.col and hex_1.sss-1 == hex_2.sss:
		return True
	elif hex_1.row-1 == hex_2.row and hex_1.col+1 == hex_2.col and hex_1.sss == hex_2.sss:
		return True
	elif hex_1.row-1 == hex_2.row and hex_1.col == hex_2.col and hex_1.sss+1 == hex_2.sss:
		return True
	elif hex_1.row == hex_2.row and hex_1.col-1 == hex_2.col and hex_1.sss+1 == hex_2.sss:
		return True
	# Determine world wrap
	return False

def game_quit():
	# Play quit sound
	pygme.quit()
	quit()