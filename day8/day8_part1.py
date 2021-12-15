import sys


def count_unique_numbers(filepath):
	result = 0
	with open(filepath, 'r') as f:
		for line in f:
			output_values = line.rpartition('|')[2].strip().split()
			for val in output_values:
				if len(val) in [2, 3, 4, 7]:
					result += 1
	return result


def main():
	print(count_unique_numbers(sys.argv[1]))


if __name__ == '__main__':
	main()
