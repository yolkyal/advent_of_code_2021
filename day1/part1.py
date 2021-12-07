import sys


def count_increases(filepath):
	increases = 0
	with open(filepath, 'r') as f:
		last_input = int(next(f))
		for val in f:
			val = int(val)
			if val > last_input:
				increases += 1
			last_input = val

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
