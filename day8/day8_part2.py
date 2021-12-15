import sys


def get_output_values(filepath):
	result = []
	with open(filepath, 'r') as f:
		for line in f:
			input_values = line.partition('|')[0].strip().split()
			output_values = line.partition('|')[2].strip().split()
			symbol_map = get_symbol_map(input_values)

			total = 0
			multiplier = 1000
			for val in output_values:	
				for number, chars in symbol_map.items():
					if set(val) == set(chars):
						total += int(number) * multiplier
						multiplier /= 10
						break
			result.append(int(total))
	return result


def get_symbol_map(vals):
	len5_set = [set(val) for val in vals if len(val) == 5]
	len6_set = [set(val) for val in vals if len(val) == 6]

	symbol_map = {}
	symbol_map[1] = set([val for val in vals if len(val) == 2][0])
	symbol_map[4] = set([val for val in vals if len(val) == 4][0])
	symbol_map[7] = set([val for val in vals if len(val) == 3][0])
	symbol_map[8] = set([val for val in vals if len(val) == 7][0])

	symbol_map[3] = set(get_match(len5_set, symbol_map[1]))
	len5_set.remove(symbol_map[3])

	symbol_map[9] = set(get_match(len6_set, symbol_map[3]))
	len6_set.remove(symbol_map[9])

	symbol_map[0] = set(get_match(len6_set, symbol_map[7]))
	len6_set.remove(symbol_map[0])

	for st in len5_set:
		if get_match([symbol_map[9]], st):
			symbol_map[5] = st
			len5_set.remove(st)
			break

	symbol_map[2] = list(len5_set)[0]
	symbol_map[6] = list(len6_set)[0]

	return symbol_map


def get_match(vals, match_set):
	for val in vals:
		if all([c in val for c in match_set]):
			return val


def main():
	print(sum([val for val in get_output_values(sys.argv[1])]))


if __name__ == '__main__':
	main()
