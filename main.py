from button import Button
import pygame
import copy
import os

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAMIN JAM")

header_font = pygame.font.Font(os.path.join("assets", "fonts", 'WinterPixelBold.otf'), 100)
credits_font = pygame.font.Font(os.path.join("assets", "fonts", 'WinterPixelBold.otf'), 20)
text_font = pygame.font.Font(None, 36)

games = ["Snake", "Minesweeper"]

palettes = [
	[(242, 242, 242), (26, 26, 26)],
	[(26, 26, 26), (242, 242, 242)]
]
colors = palettes[0]

def render_header(window, hfont, cfont, x):
	header = hfont.render("GAMIN JAM", True, colors[1])
	header_rect = header.get_rect(center=(x, 200))
	window.blit(header, header_rect)

	credits = cfont.render("made by qterisse", True, colors[1])
	credits_rect = credits.get_rect(topright=(648, 240))
	window.blit(credits, credits_rect)

def render_games_names(window, color, mouse_x, mouse_y):
	font = pygame.font.Font(None, 36)
	underline_font = pygame.font.Font(None, 36)
	underline_font.set_underline(True)

	for i, title in enumerate(games):
		text = font.render(title, True, color)
		text_rect = text.get_rect(topleft=((width // 2) + 22, 310 + (i * 40)))
		if (text_rect.collidepoint((mouse_x, mouse_y))):
			text = underline_font.render(title, True, color)
		window.blit(text, text_rect)

moving_left = 0
moving_right = 0
play_mode = False

def click_play():
	global moving_left, moving_right, play_mode

	if (play_mode):
		moving_right = 200
		play_mode = False

		buttons[0].color = colors[0]
		buttons[0].text_color = colors[1]
	else:
		moving_left = 200
		play_mode = True

		buttons[0].color = colors[1]
		buttons[0].text_color = colors[0]

buttons = [
	Button(width/2 - 100, 300, 200, 60, click_play, text="PLAY", 
		color=colors[0], hover_color=colors[1], text_color=colors[1], 
		hover_text_color=colors[0], border_color=colors[1]),
	Button(width/2 - 100, 380, 200, 60, lambda: print("Hello world!"), text="SCORES", 
		color=colors[0], hover_color=colors[1], text_color=colors[1], 
		hover_text_color=colors[0], border_color=colors[1]),
]

running = True
while running:
	mouse_x, mouse_y = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for button in buttons:
				if (button.is_focused(mouse_x, mouse_y)):
					button.click()
	
	window.fill(colors[0])

	render_header(window, header_font, credits_font, width // 2)

	for button in buttons:
		if (button.is_focused(mouse_x, mouse_y) and button.hover_color):
			button.hovered = 1
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		elif (not button.is_focused(mouse_x, mouse_y) and button.hover_color and button.hovered):
			button.hovered = 0
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
		
		button.draw(window, text_font)
	
	if (moving_left > 0):
		for button in buttons:
			button.pos = (button.pos[0] - moving_left * 0.006, button.pos[1])
		moving_left -= 1

	if (moving_right > 0):
		for button in buttons:
			button.pos = (button.pos[0] + moving_right * 0.006, button.pos[1])
		moving_right -= 1
	
	if (play_mode and moving_left >= 0 and moving_left < 100):
		shade = colors[1][0] + moving_left * 2
		color = (shade, shade, shade)
		pygame.draw.line(window, color, (width // 2, 295), (width // 2, 450), 3)
		render_games_names(window, color, mouse_x, mouse_y)

	pygame.display.flip()

pygame.quit()