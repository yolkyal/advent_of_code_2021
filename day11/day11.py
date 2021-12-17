import sys


def load_data(filepath):
	grid = dict()
	with open(filepath) as f:
		for row, line in enumerate(f):
			for col, val in enumerate(line.strip()):
				grid[(row, col)] = int(val)
	return grid


def progress(grid):
	ls_flash = []
	for k in grid:
		grid[k] += 1
		if grid[k] == 10:
			ls_flash.append(k)

	for k in ls_flash:
		flash(grid, k)

	num_flashes = 0
	for k in grid:
		if grid[k] > 9:
			grid[k] = 0
			num_flashes += 1

	return num_flashes
	

def flash(grid, k):
	grid[k] += 1
	adj_keys = [(k[0]-1, k[1]-1), (k[0], k[1]-1), (k[0]+1, k[1]-1), (k[0]+1, k[1]), (k[0]+1, k[1]+1), (k[0], k[1]+1), (k[0]-1, k[1]+1), (k[0]-1, k[1])]
	for k_ in adj_keys:
		if k_ in grid:
			grid[k_] += 1
			if grid[k_] == 10:
				flash(grid, k_)


def main():
	grid = load_data(sys.argv[1])
	for i in range(1, 1000):
		count = progress(grid)
		if count == 100:
			print(i)
			return


if __name__ == '__main__':
	main()
