import sys


openers = {']': '[', ')': '(', '}': '{', '>': '<'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
		

def get_score(line):
	stack = []
	for c in line:
		if c in ['[', '(', '{', '<']:
			stack.append(c)
		elif c in [']', ')', '}', '>']:
			if stack.pop() != openers[c]:
				return scores[c]
	return 0

def main():
	print(sum([get_score(line) for line in open(sys.argv[1])]))
	

if __name__ == '__main__':
	main()
