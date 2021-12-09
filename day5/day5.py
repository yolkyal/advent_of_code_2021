import sys


def process(filepath):
	data = []
	for i in range(1000):
		data.append([0] * 1000)
	
	with open(filepath, 'r') as f:
		for line in f:
			first, second = map(lambda x: x.split(','), line.strip().split(' -> '))
			first = [int(first[0]), int(first[1])]
			second = [int(second[0]), int(second[1])]
			if first[0] == second[0]:
				if first[1] < second[1]:
					for i in range(first[1], second[1]+1):
						data[i][first[0]] += 1
				else:
					for i in range(second[1], first[1]+1):
						data[i][first[0]] += 1
			elif first[1] == second[1]:
				if first[0] < second[0]:
					for i in range(first[0], second[0]+1):
						data[first[1]][i] += 1
				else:
					for i in range(second[0], first[0]+1):
						data[first[1]][i] += 1
			else:
				ls_y = range(first[0], second[0]+1) if first[0] < second[0] else range(first[0], second[0]-1, -1)
				ls_x = range(first[1], second[1]+1) if first[1] < second[1] else range(first[1], second[1]-1, -1)
				for x, y in zip(ls_x, ls_y):
					data[x][y] += 1
			
	result = 0
	for row in data:
		for val in row:
			if val > 1:
				result += 1
	return result

def main():
	print(process(sys.argv[1]))


if __name__ == '__main__':
	main()
