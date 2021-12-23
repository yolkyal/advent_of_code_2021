import sys


class Path:
	def __init__(self, caves, route):
		self.caves = caves
		self.route = route
	
	def get_next(self):
		ls_next = self.caves[self.route[-1:][0]]
		ls_new = []
		for next in ls_next:
			new_path = Path(self.caves, self.route + [next])
			if new_path.is_valid():
				ls_new.append(new_path)
		return ls_new
	
	def is_complete(self):
		return self.route[-1:][0] == 'end'
	
	def is_valid(self):
		small_cave_visits = {i: self.route.count(i) for i in set(self.route) if i == i.lower()}
		second_visited = False
		for cave, visits in small_cave_visits.items():
			if cave in ['start', 'end'] and visits > 1:
				return False
			elif visits > 2:
				return False
			elif visits == 2:
				if second_visited:
					return False
				else:
					second_visited = True
		return True


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
	in_progress = [Path(caves, ['start'])]
	while len(in_progress) > 0:
		ls_new = [path.get_next() for path in in_progress]
		in_progress = []
		for ls_next in ls_new:
			for path_ in ls_next:
				if path_.is_complete():
					paths.append(path_)
				else:
					in_progress.append(path_)
	return paths


def main():
	caves = load_data(sys.argv[1])
	paths = get_paths(caves)
	print(len(paths))


if __name__ == '__main__':
	main()
