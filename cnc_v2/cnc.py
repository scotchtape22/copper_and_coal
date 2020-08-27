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
							print(my_button.button_id)
							click_select = my_button
							nada = False
					if nada:
						click_select = None

		# Do something with the button presss
		if click_select:
			if click_select.button_id == "test":
				cncp.test_map()
			print(click_select.button_id)

		# Draw Display
		gameDisplay.fill(cncc.get_color("bg"))

		# Draw title
		title_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',64)
		title_text = "Copper and Coal"
		TitleSurf, TitleRect = cncc.text_objects(title_text,title_font,[153,102,51])
		TitleRect.center = ((display_width/2),100)
		gameDisplay.blit(TitleSurf,TitleRect)

		# Subtitle

		subtitle_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',32)
		subtitle_text = "By Scott Wambold"
		subTitleSurf, subTitleRect = cncc.text_objects(subtitle_text,subtitle_font,[153,102,51])
		subTitleRect.center = ((display_width/2),200)
		gameDisplay.blit(subTitleSurf,subTitleRect)

		# Draw Buttons
		for this_button in mm_buttons:
			this_button.draw(gameDisplay)



		pygame.display.update()
		clock_1.tick(60)




def make_mainmenu_buttons():
	button_font = pygame.font.Font('./fonts/steam_punk_flyer.ttf',24)
	mainmenu_buttons = []
	button_color = cncc.get_color("inactive_button")
	text_color = cncc.get_color("inactive_text")
	button_prompt_color = cncc.get_color("active_button")
	text_prompt_color = cncc.get_color("active_text")

	mainmenu_buttons.append(cncc.a_button("Test","test",button_font,[500,400,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("New Game","new",button_font,[500,500,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Load Game","load",button_font,[500,564,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Options","opt",button_font,[500,628,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
	mainmenu_buttons.append(cncc.a_button("Credits","credits",button_font,[500,692,240,64],button_color,text_color,button_prompt_color,text_prompt_color))
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

