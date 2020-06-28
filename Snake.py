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

class Block():
	def __str__(self):
		return f'{self.position}'

	def __init__(self, position=(0,0)):
		self.position = position
		self.x, self.y = position 
		self.next = None

	def set_position(self):
		self.position = self.x, self.y

	def moveX(self, right=True):
		# return where the block would've have been had it moved
		if right:
			self.x = self.x + 1

			# If you're no longer on the board
			if self.x = 10:
				self.x = 0
		else:
			self.x = self.x - 1

			# If you're no longer on the board
			if self.x == -1:
				self.x = 9

		return self.x, self.y

	def moveY(self, up=True):
		if up:
			self.y = self.y + 1

			# If you're no longer on the board
			if self.y == 10:
				self.y = 0
		else:
			self.y = self.y - 1
			# If you're no longer on the board
			if self.y == -1
				self.y = 9
		
		return self.x, self.y

	def goto(self, position):
		self.x , self.y = position
		self.set_position()

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

			# make the tail the new head
			old_head = self.head
			self.head = old_tail
			self.head.next = old_head
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
			old_head = self.head
			self.head = old_tail
			self.head.next = old_head
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

class Grid():
	def __str__(self):
		rows = [str(row) for row in self.board]
		return '\n'.join(rows)

	def __init__(self):
		global defualt
		self.board = None
		self.reset()

	def reset(self):
		global default
		self.board = [row[:] for row in default][:]

	def move(self, x,y):
		self.board[y][x] = 1

	def draw_snake(self, snake):
		self.reset()
		current = snake.head
		while current:
			self.move(current.x, current.y)
			current = current.next

		print(self)

def main():
	snake = Snake()
	snake.append()
	snake.moveX()
	snake.append()
	snake.append()
	snake.moveX()
	snake.moveX()
	snake.append()
	snake.moveY()
	myGrid = Grid()
	myGrid.draw_snake(snake)

if __name__ == "__main__":
	main()