import sys


def load_data(filepath):
	with open(filepath) as f:
		return list(map(int, next(f).split(',')))


def solve(crabs):
	fuel_cost_cache = generate_fuel_cost_cache(max(crabs) + 1)
	best = (0, get_fuel_cost(crabs, 0, fuel_cost_cache))
	for i in range(1, max(crabs)):
		cost = get_fuel_cost(crabs, i, fuel_cost_cache)
		if cost < best[1]:
			best = (i, cost)
	return best


def get_fuel_cost(crabs, target_pos, fuel_cost_cache):
	return sum([fuel_cost_cache[abs(crab - target_pos)] for crab in crabs])


def generate_fuel_cost_cache(limit):
	cache = {0: 0}
	for i in range(1, limit):
		cache[i] = cache[i-1] + i
	return cache


def main():
	crabs = load_data(sys.argv[1])
	print(solve(crabs))


if __name__ == '__main__':
	main()
