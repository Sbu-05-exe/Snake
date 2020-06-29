import pygame

# colors

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (0,255,255)
white = (255,255,255)
black = (0,0,0)

# globals

WIDTH = 500
HEIGHT = 500
WIN_SIZE = (WIDTH, HEIGHT)

rows = 10
cols = 10
row_width = int(WIDTH/rows)
col_width = int(HEIGHT/cols)
block_size = (row_width, col_width)

# Game setup
pygame.init()

win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Snake 2.0")

game = pygame.Surface(WIN_SIZE)
game.fill(black)
win.blit(game, (0,0))
pygame.display.flip()

# Import Snake after a while since the Snake modules requre some Game globals
import Snake as s

class Point:
	def __init__(self, x=0,y =0):
		self.x = x
		self.y = y

	def co_ord(self):
		return (self.x,self.y)

	def reflect(self):
		return (self.y, self.x)

	def move_Y(self, shift):
		return self.move(0,shift)

	def move_X(self, shift):
		return self.move(shift,0)

	def move(self, x1=0,y1=0):
		self.x += x1
		self.y += y1
		return (self.x, self.y)

# def draw_block(block, color):
# 	global game, col_width, row_width
# 	block.position = (co_ords.x * col_width, co_ords.y * row_width)
# 	block_size = (row_width, col_width)
# 	my_rect = pygame.Rect(position, block_size, red)
# 	pygame.draw.rect(game, color, block)

def draw_snake(snake):

	# draw the head
	head = True
	for block in snake.get_snake_blocks():
		if head:
			color = green
			head = False
		else:
			color = red

		pygame.draw.rect(game,color,block)

def draw_grid():
	global HEIGHT, rows, game
	start = Point(row_width,0)
	end = Point(row_width, HEIGHT)

	for i in range(1,rows):
		pygame.draw.line(game, white, start.co_ord(), end.co_ord())
		pygame.draw.line(game, white, start.reflect(), end.reflect())
		change_x = col_width

		start.move_X(change_x)
		end.move_X(change_x)

def render_display(snake):
	global win, game, white


	game.fill(black)
	draw_snake(snake)
	draw_grid()
	win.blit(game, (0,0))


	pygame.display.flip() 

def delay(elapsed):
	pygame.time.delay(elapsed)

def mainloop():
	# default values
	my_snake = s.Snake()
	board = s.Grid()
	
	score = 0
	horizontal = True
	forward = True
	position = (0,0)

	up = True
	down = True
	left = False
	right = True

	render_display(my_snake)

	alive = True
	while alive:
		if horizontal:
			my_snake.moveX(forward)
		else:
			my_snake.moveY(forward)

		# board.draw_snake(snake)
		render_display(my_snake)
		board.draw_snake(my_snake)
		delay(200)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				alive = False

			if event.type == pygame.KEYDOWN:
				if event.key == 13:
					my_snake.append()

				if event.key == pygame.K_UP:
					if up:
						horizontal = False
						forward = True
						
					
						down = False
						left = True
						right = True

				if event.key == pygame.K_DOWN:
					if down:
						horizontal = False
						forward = False
					
						up = False
						left = True
						right = True

				if event.key == pygame.K_LEFT:
					if left:
						horizontal = True
						forward = False
					
						right = False
						up = True
						down = True

				if event.key == pygame.K_RIGHT:
					if right:
						horizontal = True
						forward = True

						left = False
						up = True
						down = True


	print('GAME OVER')
	pygame.quit()

def main():	
	mainloop()

if __name__ == "__main__":
	main()