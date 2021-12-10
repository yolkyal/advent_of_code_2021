import sys


openers = {']': '[', ')': '(', '}': '{', '>': '<'}
scores = {'(': 1, '[': 2, '{': 3, '<': 4}


def get_lines_scores(filepath):
	result = []
	for line in open(filepath):
		stack = []
		for c in line:
			if c in ['[', '(', '{', '<']:
				stack.append(c)
			elif c in [']', ')', '}', '>']:
				if stack.pop() != openers[c]:
					stack = []
					break
		if stack:
			result.append(get_stack_score(stack))
	return result


def get_stack_score(stack):
	result = 0
	for c in reversed(stack):
		result *= 5
		result += scores[c]
	return result


def main():
	scores = get_lines_scores(sys.argv[1])
	winner_score = sorted(scores)[int(len(scores) / 2)]
	print(winner_score)
	

if __name__ == '__main__':
	main()
