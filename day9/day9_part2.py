import sys


def load_data(filepath):
	grid = {}
	with open(filepath) as f:
		row = 0
		for line in f:
			col = 0
			for val in list(line.strip()):
				grid[(row, col)] = int(val)
				col += 1
			row += 1
	return grid


def find_basins(grid):
	basins = []
	in_basin = set()
	for k, v in grid.items():
		if k not in in_basin and v < 9:
			basin = get_basin(grid, k, {k})
			basins.append(basin)
			for k_ in basin:
				in_basin.add(k_)
	return basins


def get_basin(grid, k, basin):
	ls_adj = [k_ for k_ in [(k[0]+1, k[1]), (k[0]-1, k[1]), (k[0], k[1]+1), (k[0], k[1]-1)] if k_ in grid]
	for k_ in ls_adj:
		if grid[k_] < 9 and k_ not in basin:
			basin.add(k_)
			basin = get_basin(grid, k_, basin)
	return basin


def main():
	grid = load_data(sys.argv[1])
	basins = find_basins(grid)
	basin_sizes = [len(basin) for basin in basins]
	basin_sizes.sort()
	result = basin_sizes[-1:][0] * basin_sizes[-2:-1][0] * basin_sizes[-3:-2][0]
	print(result)


if __name__ == '__main__':
	main()
