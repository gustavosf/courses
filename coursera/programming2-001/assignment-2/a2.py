# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
	def __init__(self, symbol, row, col):
		self.symbol = symbol
		self.set_location(row, col);
		self.num_sprouts_eaten = 0
	def set_location(self, row, col):
		self.row = row
		self.col = col
	def eat_sprout(self):
		self.num_sprouts_eaten += 1
	def __str__(self):
		return "%s at (%d, %d) ate %d sprouts." % \
			(self.symbol, self.row, self.column, self.num_sprouts_eaten)


class Maze:
	""" A 2D maze. """
	def __init__(self, maze, rat_1, rat_2):
		self.maze = maze
		self.rat_1 = rat_1
		self.rat_2 = rat_2
		self.num_sprouts_left = sum(x.count(SPROUT) for x in maze)
	def is_wall(self, row, col):
		return maze[row][col] == WALL
	def get_character(self, row, col):
		if self.rat_1.row == row and self.rat_1.col == col:
			return RAT_1_CHAR
		elif self.rat_2.row == row and self.rat_2.col == col:
			return RAT_2_CHAR
		else:
			return maze[row][col]
	def move(self, rat, row, col):
		pos_x = rat.row + row
		pos_y = rat.col + col
		if (not self.is_wall(row, col)):
			rat.set_location(pos_x, pos_y)
			if (self.maze[pos_x, pos_y] == SPROUT):
				rat.eat_sprout
				self.num_sprouts_eaten -= 1
				self.maze[pos_x, pos_y] = HALL
			return True
		return False
	def __str__(self):
		output = ''
		maze = self.maze
		maze[self.rat_1.x][self.rat_1.y] = RAT_1_CHAR
		maze[self.rat_2.x][self.rat_2.y] = RAT_2_CHAR
		for line in maze:
			output += ''.join(maze) + '\n'
		output += self.rat_1 + '\n' + self.rat_2,
		return output