import sys


def load_timer_counts(filepath):
	with open(filepath, 'r') as f:
		timers = [int(val) for val in next(f).split(',')]
		return {i: timers.count(i) for i in range(9)}


def progress(timer_counts):
	new_timer_counts = {8: timer_counts[0]}
	for i in range(0, 8):
		new_timer_counts[i] = timer_counts[i+1]
	new_timer_counts[6] += new_timer_counts[8]
	return new_timer_counts


def main():
	timer_counts = load_timer_counts(sys.argv[1])
	for i in range(int(sys.argv[2])):
		timer_counts = progress(timer_counts)
	print(sum(timer_counts.values()))


if __name__ == '__main__':
	main()
