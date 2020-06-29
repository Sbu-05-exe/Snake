import pygame
from pygame import Rect
from Game import col_width, row_width, block_size, game

default = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0]
]

class Block(Rect):
	def __bool__(self):
		return self.bool

	def __str__(self):
		return f'{self.position}'

	def __init__(self, position=(0,0), next = None):
		self.position = position
		self.x, self.y = position 
		self.next = None
		self.bool = True
		self.set_block()

	def get_block(self):
		return self.Block

	def set_block(self):
		position = row_width * self.x,col_width * self.y
		block_size = (row_width, col_width)

		self.Block = pygame.Rect(position, (row_width,col_width))

	def set_position(self):
		self.position = self.x, self.y

	def moveX(self, right=True):
		# return where the block would've have been had it moved
		if right:
			x = self.x + 1

			# If you're no longer on the board
			if x == 10:
				x = 0
		else:
			x = self.x - 1

			# If you're no longer on the board
			if x == -1:
				x = 9

		return x, self.y

	def moveY(self, up=True):
		if up:
			y = self.y - 1
			# If you're no longer on the board
			if y == -1:
				y = 9
		else:
			y = self.y + 1
			# If you're no longer on the board
			if y == 10:
				y = 0
		
		print(self.x, y)
		return self.x, y

	def goto(self, position):
		self.x, self.y = position
		self.set_position()
		self.set_block()

class Snake():
	def __str__(self):
		current = self.head
		result = [str(self.head)]

		while current.next:
			current = current.next
			result.append(str(current))

		return '\n'.join(result)

	def __init__(self):
		self.head = Block()
		self.length = 1
		self.appending = False

	def moveX(self,forward=True):
		if self.length == 1:
			self.head.goto(self.head.moveX(forward))
		# Get the position of the head if it moved
		else: 
			head_pos = self.head.moveX(forward)

			# get the last 2 blocks of the snake
			current = self.head
			while current.next:
				new_tail = current
				current = current.next

			# move the snake to where the head was going to go
			old_tail = current
			old_tail.goto(head_pos)

			# make the old tail the new head
			old_tail.next = self.head
			self.head = old_tail
			new_tail.next = None

	def moveY(self,forward=True):
		if self.length == 1:
			self.head.goto(self.head.moveY(forward))
		# Get the position of the head if it moved
		else: 
			head_pos = self.head.moveY(forward)

			# get the last 2 blocks of the snake
			current = self.head
			while current.next:
				new_tail = current
				current = current.next

			# move the snake to where the head was going to go
			old_tail = current
			old_tail.goto(head_pos)

			# make the tail the new head
			old_tail.next = self.head
			self.head = old_tail
			new_tail.next = None

	def append(self):
		current = self.head
		while current.next:
			current = current.next

		# New tail Takes up the position of the old tail block
		old_tail = current
		new_tail = Block(old_tail.position)
		old_tail.next = new_tail 
		self.appending = True
		self.length = self.length + 1
		self.tail = new_tail

	def prune(self, position):
		current = self.head
		for i in range(position):
			current = current.next

		current.next = None

	def get_head(self):
		return self.head

	def get_tail(self):
		return self.tail

	def get_length(self):
		return self.length

	def get_snake_blocks(self):
		result = []
		current = self.head

		while current:
			result.append(current.get_block())
			current = current.next

		return result

class Grid():
	def __str__(self):
		rows = [str(row) for row in self.board]
		board = '\n'.join(rows) 
		return '================================= \n' + board

	def __init__(self):
		global defualt
		self.board = None
		self.reset()

	def reset(self):
		global default
		self.board = [row[:] for row in default][:]

	def get_pos(self, x, y):
		return self.board[y][x]

	def is_empty(self,x,y):
		return self.board[y][x] == 0

	def move(self, x,y, num):
		self.board[y][x] = num

	def draw_snake(self, snake):
		self.reset()
		current = snake.head
		i = 1
		
		overlap = False
		while current.next and not(overlap):
			x,y = current.x, current.y

			if self.is_empty(x,y):
				self.move(x, y, i)

			else:
				overlap = True
				snake.prune(i)
			
			current = current.next
			i = i + 1

		print(self)

def main():
	# Testing if the classes work
	snake = Snake()
	snake.moveX()
	snake.append()
	snake.moveX()
	snake.append()
	snake.append()
	snake.moveX()
	snake.moveX()
	snake.append()
	snake.append()
	snake.moveX()
	snake.moveY(False)
	snake.moveY(False)
	myGrid = Grid()
	myGrid.draw_snake(snake)

if __name__ == "__main__":
	main()