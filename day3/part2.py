import sys


def get_val_most_common_bit_func(filepath, func):
	with open(filepath) as f:
		vals = [line.strip() for line in f]

	bit_index = 0
	while len(vals) > 1:
		most_common_bit = get_most_common_bit(vals, bit_index)
		vals = [val for val in vals if func(val[bit_index], most_common_bit)]
		bit_index += 1
	return vals[0]


def get_most_common_bit(vals, bit_index):
	ones_count = 0
	for val in vals:
		if val[bit_index] == '1':
			ones_count += 1
	return '1' if ones_count >= len(vals) / 2 else '0'


def bin_to_dec(bin):
	return sum([2**i for i, c in enumerate(reversed(list(bin))) if c == '1'])


def main():
	print('Starting...')
	if len(sys.argv) == 2:
		oxygen = get_val_most_common_bit_func(sys.argv[1], lambda x, y: x == y)
		co2 = get_val_most_common_bit_func(sys.argv[1], lambda x, y: x != y)
		result = bin_to_dec(oxygen) * bin_to_dec(co2)
		print('Success!', 'Result:', result)
	else:
		print('Program requires exactly one parameter which is the input filepath')
	print('Exiting...')
		

if __name__ == '__main__':
	main()
