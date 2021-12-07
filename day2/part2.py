import sys


def calculate_horiz_depth(filepath):
	horiz, depth, aim = 0, 0, 0
	with open(filepath, 'r') as f:
		for line in f:
			command, val = line.split()
			val = int(val)
			if command == 'forward':
				horiz += val
				depth += aim * val
			elif command == 'up':
				aim -= val
			elif command == 'down':
				aim += val
	return horiz, depth


def main():
	print('Starting...')
	if len(sys.argv) == 2:
		horiz, depth = calculate_horiz_depth(sys.argv[1])
		result = horiz * depth
		print('Success!', 'Result:', result)
	else:
		print('Program requires exactly one parameter which is the input filepath')
	print('Exiting...')
		

if __name__ == '__main__':
	main()
	
