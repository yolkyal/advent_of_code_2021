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


def find_low_points(grid):
	low_points = []
	for k, v in grid.items():
		ls_adj = [k_ for k_ in [(k[0]+1, k[1]), (k[0]-1, k[1]), (k[0], k[1]+1), (k[0], k[1]-1)] if k_ in grid]
		ls_vals = [grid[k_] for k_ in ls_adj]
		if all([v_ > v for v_ in ls_vals]):
			low_points.append((k, v))
	return low_points


def main():
	grid = load_data(sys.argv[1])
	low_points = find_low_points(grid)
	print(sum([low_point[1] + 1 for low_point in low_points]))


if __name__ == '__main__':
	main()
