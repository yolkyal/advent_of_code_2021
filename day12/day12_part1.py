import sys


def load_data(filepath):
	caves = dict()
	for line in open(filepath):
		start, end = line.strip().split('-')
		if start in caves:
			caves[start] += [end]
		else:
			caves[start] = [end]
		if end in caves:
			caves[end] += [start]
		else:
			caves[end] = [start]
	return caves


def get_paths(caves):
	paths = []
	in_progress = [['start']]
	while len(in_progress) > 0:
		in_progress = progress(in_progress, caves)
		for path_ in in_progress:
			if path_[-1:][0] == 'end':
				paths.append(path_)
		for path_ in paths:
			if path_ in in_progress:
				in_progress.remove(path_)
	return paths


def progress(paths, caves):
	new_paths = []
	for path in paths:
		end = path[-1:][0]
		ls_next = caves[end]
		for next in ls_next:
			if next == next.lower() and next in path:
				continue
			else:
				new_paths.append(path + [next])
	return new_paths


def main():
	caves = load_data(sys.argv[1])
	for path in get_paths(caves):
		print(path)


if __name__ == '__main__':
	main()
