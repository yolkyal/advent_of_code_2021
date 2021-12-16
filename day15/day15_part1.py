import sys
import math


def load_data(filepath):
	row_num, col_num = 0, 0
	graph = {}
	with open(filepath) as f:
		row = 0
		for line in f:
			col = 0
			for val in list(line.strip()):
				graph[(row, col)] = int(val)
				col += 1
			col_num = col
			row += 1
		row_num = row
	return graph, row_num, col_num


def dijkstra(graph, source, target):
	unreached = set()
	
	dist = {}
	for vertex in graph:
		dist[vertex] = 10000000
		unreached.add(vertex)
	dist[source] = 0

	endpoints = {(source)}
	
	while len(unreached) > 0:
		u = (None, 10000000)
		for vertex in endpoints:
			dist_v = dist[vertex]
			if dist_v < u[1]:
				u = (vertex, dist_v)
		u = u[0]
		
		unreached.remove(u)
		endpoints.remove(u)
		if u == target:
			return dist[u]
		
		for v in [(u[0]+1, u[1]), (u[0], u[1]+1), (u[0]-1, u[1]), (u[0], u[1]-1)]:
			if v in unreached:
				endpoints.add(v)
				alt = dist[u] + graph[v]
				if alt < dist[v]:
					dist[v] = alt


def main():
	graph, row_num, col_num = load_data(sys.argv[1])
	source = (0, 0)
	target = (row_num * 5 - 1, col_num * 5 - 1)
	result = dijkstra(graph, source, target)
	print(result)


if __name__== '__main__':
	main()
