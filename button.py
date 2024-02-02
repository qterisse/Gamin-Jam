import pygame

class Button:

	def __init__(self, x: int, y: int, width: int, height: int,
			action, text: str=None, text_color: tuple=(26, 26, 26),
			color: tuple=(242, 242, 242), border_radius: int=12,
			hover_color: tuple=(26, 26, 26), 
			hover_text_color: tuple=(242, 242, 242),
			border_color: tuple=(26, 26, 26), border_size: int=3):
		self.pos = (x, y)
		self.size = (width, height)
		self.action = action
		self.text = text
		self.text_color = text_color
		self.color = color
		self.border_radius = border_radius
		self.hover_color = hover_color
		self.hover_text_color = hover_text_color
		self.hovered = 0
		self.border_color = border_color
		self.border_size = border_size
	
	def draw(self, window, font:pygame.font.Font=None):
		pygame.draw.rect(
			window, 
			self.color if not self.hovered else self.hover_color, 
			(self.pos[0], self.pos[1], self.size[0], self.size[1]), 
			border_radius=self.border_radius
		)

		if (self.border_color):
			pygame.draw.rect(
				window, 
				self.border_color, 
				(self.pos[0], self.pos[1], self.size[0], self.size[1]), 
				border_radius=self.border_radius,
				width=self.border_size
			)

		if (self.text and font):
			text = font.render(
				self.text, 
				True, 
				self.text_color if not self.hovered else self.hover_text_color
			)
			text_rect = text.get_rect(center=(
				self.pos[0] + self.size[0] // 2, 
				self.pos[1] + self.size[1] // 2
			))
			window.blit(text, text_rect)

	def is_focused(self, x, y):
		return (
			x >= self.pos[0] and
			x <= self.pos[0] + self.size[0] and
			y >= self.pos[1] and
			y <= self.pos[1] + self.size[1]
		)

	def click(self):
		if (self.action):
			self.action()
