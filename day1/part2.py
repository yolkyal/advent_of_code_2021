import sys


def count_increases(filepath):
	increases = 0
	with open(filepath, 'r') as f:
		tmp, first_input, second_input = int(next(f)), int(next(f)), int(next(f))
		last_sum = tmp + first_input + second_input
		for val in f:
			val = int(val)
			cur_sum = first_input + second_input + val
			if cur_sum > last_sum:
				increases += 1
			first_input = second_input
			second_input = val
			last_sum = cur_sum

	return increases


def main():
	print('Starting...')
	if len(sys.argv) == 2:
		result = count_increases(sys.argv[1])
		print('Success!', 'Result:', result)
	else:
		print('Program requires exactly one parameter which is the input filepath')
	print('Exiting...')
		

if __name__ == '__main__':
	main()
