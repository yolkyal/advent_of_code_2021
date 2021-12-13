import sys


def load_data(filepath):
	dots = set()
	with open(filepath, 'r') as f:
		for line in f:
			if line != '\n':
				x, y = line.strip().split(',')
				dots.add((int(x), int(y)))
			else:
				break

		folds = []
		for line in f:
			c, val = line.strip().replace('fold along ', '').split('=')
			folds.append((c, int(val)))

	return dots, folds


def apply_fold(dots, fold):
	new_dots = set()
	if fold[0] == 'x':
		for dot in dots:
			if dot[0] > fold[1]:
				new_dots.add((fold[1] - (dot[0] - fold[1]), dot[1]))
			elif dot[0] < fold[1]:
				new_dots.add(dot)
	elif fold[0] == 'y':
		for dot in dots:
			if dot[1] > fold[1]:
				new_dots.add((dot[0], fold[1] - (dot[1] - fold[1])))
			elif dot[1] < fold[1]:
				new_dots.add(dot)
	return new_dots


def print_(dots):
	max_x, max_y = -1, -1
	for dot in dots:
		max_x = max(max_x, dot[0])
		max_y = max(max_y, dot[1])
	
	dots_arr = []
	for i in range(max_y + 1):
		dots_arr.append(['.'] * (max_x + 1))

	for dot in dots:
		dots_arr[dot[1]][dot[0]] = '#'

	for line in dots_arr:
		print(''.join(line))


def main():
	dots, folds = load_data(sys.argv[1])
	for fold in folds:
		dots = apply_fold(dots, fold)
	print_(dots)


if __name__ == '__main__':
	main()
