import sys


def load_data(filepath):
	with open(filepath) as f:
		return list(map(int, next(f).split(',')))


def solve(crabs):
	best = (0, get_fuel_cost(crabs, 0))
	for i in range(1, max(crabs)):
		cost = get_fuel_cost(crabs, i)
		if cost < best[1]:
			best = (i, cost)
	return best


def get_fuel_cost(crabs, target_pos):
	return sum([abs(crab - target_pos) for crab in crabs])


def main():
	crabs = load_data(sys.argv[1])
	print(solve(crabs))


if __name__ == '__main__':
	main()
