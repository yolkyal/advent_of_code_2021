import sys


def get_winner_score(draw, grids):
	for val in draw:
		for grid in grids:
			fill(grid, val)
			if is_won(grid):
				return get_score(grid, val)


def get_loser_score(draw, grids):
	for val in draw:
		if len(grids) > 1:
			for grid in grids:
				fill(grid, val)
			grids = [grid for grid in grids if not is_won(grid)]
		else:
			fill(grids[0], val)
			if is_won(grids[0]):
				return get_score(grids[0], val)


def load_data(filepath):
	with open(filepath, 'r') as f:
		data = [line.strip() for line in f if line != '\n']
		draw = load_draw(data[0])
		grids = [load_grid(data[i:i+6]) for i in range(1, len(data), 5)]
	return draw, grids


def load_draw(data):
	return [int(val) for val in data.split(',')]

	
def load_grid(data):
	grid = []
	for line in data:
		grid.append([[int(val), False] for val in line.split()])
	return grid


def fill(grid, val):
	for row in range(5):
		for col in range(5):
			if grid[row][col][0] == val:
				grid[row][col][1] = True


def is_won(grid):
	for row in range(5):
		if all([grid[row][i][1] for i in range(5)]):
			return True
	for col in range(5):
		if all([grid[i][col][1] for i in range(5)]):
			return True
	return False


def get_score(grid, winning_val):
	return sum([grid[x][y][0] for x in range(5) for y in range(5) if not grid[x][y][1]]) * winning_val


def main():
	draw, grids = load_data(sys.argv[1])
	print('Winner:', get_winner_score(draw, grids), 'Loser:', get_loser_score(draw, grids))


if __name__ == '__main__':
	main()
