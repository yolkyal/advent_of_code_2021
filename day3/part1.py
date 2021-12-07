import sys


def get_gamma_epsilon(filepath):
	bit_count = {}
	line_count = 0
	with open(filepath) as f:
		for line in f:
			line_count += 1
			for col_num, bit in enumerate(line.strip()):
				bit_count[col_num] = bit_count.get(col_num, 0) + int(bit)

	gamma, epsilon = 0, 0
	half_line_count = line_count / 2
	for i, val in enumerate(reversed(list(bit_count.values()))):
		if val > half_line_count:
			gamma += 2**i
		else:
			epsilon += 2**i
	return gamma, epsilon


def main():
	print('Starting...')
	if len(sys.argv) == 2:
		gamma, epsilon = get_gamma_epsilon(sys.argv[1])
		result = gamma * epsilon
		print('Success!', 'Result:', result)
	else:
		print('Program requires exactly one parameter which is the input filepath')
	print('Exiting...')
		

if __name__ == '__main__':
	main()
