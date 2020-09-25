#!/bin/python


import pygame
import cnc_classes as cncc
import cnc_player as cncp

# Copper and Coal Wrapper

# Main Menu
# Jump to different Games
# Options Include
# new game
# load game
# options
# credits

def draw_main(mm_buttons,gameDisplay):
	intro = True
	click_select = None

	# Draw title
	title_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',64)
	title_text = "Copper and Coal"
	TitleSurf, TitleRect = cncc.text_objects(title_text,title_font,[153,102,51])
	TitleRect.center = ((display_width/2),100)

	# Subtitle
	subtitle_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',32)
	subtitle_text = "By Scott Wambold"
	subTitleSurf, subTitleRect = cncc.text_objects(subtitle_text,subtitle_font,[153,102,51])
	subTitleRect.center = ((display_width/2),200)
	

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				cncc.game_quit()

			# Only looking for a click
			if event.type == pygame.MOUSEBUTTONUP:
				x,y = event.pos
				if event.button == 1:
					nada = True
					# Check if it was a hex
					for my_button in mm_buttons:
						if my_button.but_rect.collidepoint(x,y):
							# print(my_button.button_id)
							click_select = my_button
							nada = False
					if nada:
						click_select = None

		# Do something with the button presss
		if click_select:
			if click_select.button_id == "test":
				cncp.test_map()
			if click_select.button_id == "new":
				make_game(gameDisplay,clock_1,mm_buttons)
			print(click_select.button_id)

		# Draw Display
		gameDisplay.fill(cncc.get_color("bg"))

		gameDisplay.blit(TitleSurf,TitleRect)
		gameDisplay.blit(subTitleSurf,subTitleRect)

		# Draw Buttons
		for this_button in mm_buttons:
			this_button.draw(gameDisplay)



		pygame.display.update()
		clock_1.tick(90)



def make_game(gameDisplay,clock_1,mm_buttons):
	custom_menu = []
	frequency_menu = []

	button_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',18)
	mainmenu_buttons = []
	button_color = cncc.get_color("inactive_button")
	text_color = cncc.get_color("inactive_text")
	button_prompt_color = cncc.get_color("active_button")
	text_prompt_color = cncc.get_color("active_text")
	button_select_color = cncc.get_color("selected_button")
	text_select_color = cncc.get_color("selected_text")

	# Game Options
	# Game Name
	# Game Password
	# Player Count
		# 6 or 8
	custom_menu.append(cncc.a_button("6","pc_6",None,button_font,[608,256,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("8","pc_8",None,button_font,[672,256,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	# Messaging
		# Standard
		# Airwaves (Broadcast All)
		# Grey
		# Radio Silence
	custom_menu.append(cncc.a_button("Standard","comm_standard",None,button_font,[400,352,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("Open Airwaves","comm_airwaves",None,button_font,[528,352,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("Grey Comms","comm_grey",None,button_font,[656,352,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("Radio Silence","comm_silence",None,button_font,[784,352,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	# Game Length
		# Short - 2 components
		# Medium - 3 components
		# Long - 5 Components
	custom_menu.append(cncc.a_button("Short","cp_2",None,button_font,[512,448,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("Medium","cp_3",None,button_font,[640,448,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("Long","cp_5",None,button_font,[768,448,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	# Turn Length
		# Quick
		# Marathon
	custom_menu.append(cncc.a_button("Quick","clock_quick",None,button_font,[528,544,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	custom_menu.append(cncc.a_button("Marathon","clock_long",None,button_font,[656,544,128,48],button_color,text_color,button_prompt_color,text_prompt_color))
	# If marathon - turn pauses
	frequency_menu.append(cncc.a_button("Mn","sd_mn",None,button_font,[416,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	frequency_menu.append(cncc.a_button("Tu","sd_tu",None,button_font,[480,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	frequency_menu.append(cncc.a_button("Wd","sd_wd",None,button_font,[544,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	frequency_menu.append(cncc.a_button("Th","sd_th",None,button_font,[608,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	frequency_menu.append(cncc.a_button("Fr","sd_fr",None,button_font,[672,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	frequency_menu.append(cncc.a_button("Sa","sd_sa",None,button_font,[736,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))
	frequency_menu.append(cncc.a_button("Su","sd_su",None,button_font,[800,640,64,48],button_color,text_color,button_prompt_color,text_prompt_color))

	# Launch game button
	custom_menu.append(cncc.a_button("Launch Game!","launch",None,button_font,[480,688,256,64],button_color,text_color,button_prompt_color,text_prompt_color))

	# TODO: Add back button
	custom_menu.append(cncc.a_button("Back","back",None,button_font,[64,64,128,64],button_color,text_color,button_prompt_color,text_prompt_color))

	title_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',32)
	title_text = "New Custom Game"
	TitleSurf, TitleRect = cncc.text_objects(title_text,title_font,[153,102,51])
	# TODO: Pass along display info
	TitleRect.center = ((1280/2),50)

	playing = True
	click_select = None

	# Game parameters is the returned value to the map maker
	# [name,passowrd,player_count,communication,score,clock,turn_frequency]

	game_params = ["","","","","","","",[]]

	while playing:

		gameDisplay.blit(TitleSurf,TitleRect)	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				cncc.game_quit()

			# Only looking for a click
			if event.type == pygame.MOUSEBUTTONUP:
				x,y = event.pos
				if event.button == 1:
					nada = True
					# Check if it was a hex
					for my_button in custom_menu:
						if my_button.but_rect.collidepoint(x,y):
							# Find out what type of button was clicked and put the correct id in the game params
							if my_button.button_id.startswith("pc_"):
								game_params[2] = my_button.button_id
							elif my_button.button_id.startswith("comm_"):
								game_params[3] = my_button.button_id
							elif my_button.button_id.startswith("cp_"):
								game_params[4] = my_button.button_id
							elif my_button.button_id.startswith("clock_"):
								game_params[5] = my_button.button_id
							elif my_button.button_id == "launch":
								print(game_params)
							elif my_button.button_id == "back":
								draw_main(mm_buttons,gameDisplay)
							click_select = my_button
							nada = False
					if nada:
						click_select = None

		# Do something with the button presss
		if click_select:
			pass

		# Draw Display
		gameDisplay.fill(cncc.get_color("bg"))

		gameDisplay.blit(TitleSurf,TitleRect)

		# Draw lables
		cncc.draw_notice(gameDisplay,"Player Count",button_font,[640,208,128,48],[30,30,30],[200,200,200],None)
		cncc.draw_notice(gameDisplay,"Comms Style",button_font,[640,304,128,48],[30,30,30],[200,200,200],None)
		cncc.draw_notice(gameDisplay,"Game Length",button_font,[640,400,128,48],[30,30,30],[200,200,200],None)
		cncc.draw_notice(gameDisplay,"Turn Length",button_font,[640,496,128,48],[30,30,30],[200,200,200],None)

		# Draw Buttons
		for this_button in custom_menu:
			# Skip selected button
			if this_button.button_id in game_params:
				cncc.draw_notice(gameDisplay,this_button.message,button_font,this_button.button_dem,button_select_color,text_select_color)
				continue
			this_button.draw(gameDisplay)
			# 	def __init__(self,message,button_id,data,font,button_dem,sq_co=[255,255,255],tx_co=[0,0,0],sq_p_co=[255,255,255],tx_p_co=[0,0,0],img_file=None):

		# If a marathon game is selected, draw the frequency buttons to record their responses

		pygame.display.update()
		clock_1.tick(90)

def make_mainmenu_buttons():
	button_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',24)
	mainmenu_buttons = []
	button_color = cncc.get_color("inactive_button")
	text_color = cncc.get_color("inactive_text")
	button_prompt_color = cncc.get_color("active_button")
	text_prompt_color = cncc.get_color("active_text")

	mainmenu_buttons.append(cncc.a_button("Test","test",None,button_font,[500,372,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("New Game","new",None,button_font,[500,436,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Join Game","join",None,button_font,[500,500,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Load Game","load",None,button_font,[500,564,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Options","opt",None,button_font,[500,628,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Credits","credits",None,button_font,[500,692,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	return mainmenu_buttons


if __name__ == "__main__":
	pygame.init()

	# Display will eventually come from a config file?
	display_width = 1280
	display_height = 800

	playing = True


	gameDisplay = pygame.display.set_mode([display_width,display_height])

	# Game Window Title
	pygame.display.set_caption('Copper and Coal')

	# Set FPS Clock
	# Other clocks for order timing
	clock_1 = pygame.time.Clock()

	mm_buttons = make_mainmenu_buttons()

	while playing:
		draw_main(mm_buttons,gameDisplay)

