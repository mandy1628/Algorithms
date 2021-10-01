from sys import maxsize
from typing import List

# stores the found edges
found = []

# stores the number of nodes
N = 0

# stores the capacity of each edge
cap = []

flow = []

# stores the cost per unit flow of each edge
cost = []

# stores the distance from each node and picked edges for each node
dad = []
dist = []
pi = []

INF = maxsize // 2 - 1

# function to check if it is possible to have a flow from the src to sink
def search(src: int, sink: int) -> bool:

	# initialise found[] to false
	found = [False for _ in range(N)]

	# initialise the dist[] to INF
	dist = [INF for _ in range(N + 1)]

	# distance from the source node
	dist[src] = 0

	# iterate untill src reaches N
	while (src != N):
		best = N
		found[src] = True

		for k in range(N):

			# if already found
			if (found[k]):
				continue

			# evaluate while flow is still in supply
			if (flow[k][src] != 0):

				# obtain the total value
				val = (dist[src] + pi[src] -
						pi[k] - cost[k][src])

				# if dist[k] is > minimum value
				if (dist[k] > val):
					dist[k] = val
					dad[k] = src

			if (flow[src][k] < cap[src][k]):
				val = (dist[src] + pi[src] -
						pi[k] + cost[src][k])

				# if dist[k] is > minimum value
				if (dist[k] > val):

					# Update
					dist[k] = val
					dad[k] = src

			if (dist[k] < dist[best]):
				best = k

		# update src to best for next iteration
		src = best

	for k in range(N):
		pi[k] = min(pi[k] + dist[k], INF)

	# return the value obtained at sink
	return found[sink]

# function to obtain the maximum Flow
def getMaxFlow(capi: List[List[int]],
			costi: List[List[int]],
			src: int, sink: int) -> List[int]:

	global cap, cost, found, dist, pi, N, flow, dad
	cap = capi
	cost = costi

	N = len(capi)
	found = [False for _ in range(N)]
	flow = [[0 for _ in range(N)]
			for _ in range(N)]
	dist = [INF for _ in range(N + 1)]
	dad = [0 for _ in range(N)]
	pi = [0 for _ in range(N)]

	totflow = 0
	totcost = 0

	# if a path exist from src to sink
	while (search(src, sink)):

		# set the default amount
		amt = INF
		x = sink
		
		while x != src:
			amt = min(
				amt, flow[x][dad[x]] if
				(flow[x][dad[x]] != 0) else
				cap[dad[x]][x] - flow[dad[x]][x])
			x = dad[x]

		x = sink
		
		while x != src:
			if (flow[x][dad[x]] != 0):
				flow[x][dad[x]] -= amt
				totcost -= amt * cost[x][dad[x]]

			else:
				flow[dad[x]][x] += amt
				totcost += amt * cost[dad[x]][x]
				
			x = dad[x]

		totflow += amt

	# return pair total cost and sink
	return [totflow, totcost]

# driver Code
if __name__ == "__main__":

	s = 0
	t = 4

	cap = [ [ 0, 3, 1, 0, 3 ],
			[ 0, 0, 2, 0, 0 ],
			[ 0, 0, 0, 1, 6 ],
			[ 0, 0, 0, 0, 2 ],
			[ 0, 0, 0, 0, 0 ] ]

	cost = [ [ 0, 1, 0, 0, 2 ],
			[ 0, 0, 0, 3, 0 ],
			[ 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 1 ],
			[ 0, 0, 0, 0, 0 ] ]

	ret = getMaxFlow(cap, cost, s, t)

	print("{} {}".format(ret[0], ret[1]))
