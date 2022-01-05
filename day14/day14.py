import sys


def load_data(filepath):
	with open(filepath) as f:
		template = next(f).strip()
		next(f)
		rules = {}
		for line in f:
			first, second = line.strip().split(' -> ')
			rules[first] = second
		return template, rules


def progress(pair_counts, rules):
	new_pair_counts = {}
	for pair, count in pair_counts.items():
		result = rules[pair]
		first = pair[0] + rules[pair]
		second = rules[pair] + pair[1]
		new_pair_counts[first] = new_pair_counts.get(first, 0) + count
		new_pair_counts[second] = new_pair_counts.get(second, 0) + count
	return new_pair_counts


def get_char_counts(pair_counts, first_char, last_char):
	char_counts = {}
	for pair, count in pair_counts.items():
		c1, c2 = pair[0], pair[1]
		char_counts[c1] = char_counts.get(c1, 0) + count
		char_counts[c2] = char_counts.get(c2, 0) + count
	
	for char, count in char_counts.items():
		char_counts[char] = int(char_counts[char] / 2)
	
	char_counts[first_char] += 1
	char_counts[last_char] += 1
	
	return char_counts


def get_most_least_common(char_counts):
	most_common = ('', -1)
	least_common = ('', 10**100)
	for char, count, in char_counts.items():
		if count > most_common[1]:
			most_common = (char, count)
		if count < least_common[1]:
			least_common = (char, count)
	return most_common, least_common


def main():
	template, rules = load_data(sys.argv[1])
	pairs = [template[i:i+2] for i in range(len(template) - 1)]
	pair_counts = {pair: pairs.count(pair) for pair in pairs}
	first_char, last_char = template[0], template[len(template) - 1]
	for i in range(int(sys.argv[2])):
		pair_counts = progress(pair_counts, rules)
	char_counts = get_char_counts(pair_counts, first_char, last_char)
	most_common, least_common = get_most_least_common(char_counts)
	print(most_common[1] - least_common[1])


if __name__ == '__main__':
	main()
