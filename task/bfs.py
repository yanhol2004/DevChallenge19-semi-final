from collections import deque

def common_topics(person, topics):
	return set(topics).issubset(set(person.topics))

def bfs_of_receivers(network, topics, from_person_id, min_trust_level):
	receivers = {} # from_person: [to_persons]
	visited = {} #true-visited node, false-didnt
	queue = deque() #nodes to visit
	for id in network:
		visited[id]=False

	queue.append(from_person_id)
	visited[from_person_id] = True
	while queue: #return true if queue is not empty, and false otherwise
		curr_id = queue.popleft()
		for connection_id, trust_level in network[curr_id].connections.items():
			if not visited[connection_id] and trust_level >= min_trust_level and common_topics(network[connection_id], topics):
				if curr_id not in receivers:
					receivers[curr_id] = []
				receivers[curr_id].append(connection_id)
				queue.append(connection_id)
				visited[connection_id] = True
	return receivers

def bfs_shortest_path(network, topics, from_person_id, min_trust_level):
	visited = {id: [] for id in network} # list of previously visited nodes as value, id as key
	queue = deque() #nodes to visit

	queue.append(from_person_id)
	visited[from_person_id].append(from_person_id)
	print(visited)
	while queue: #while queue is not empty
		curr_id = queue.popleft()
		for connection_id, trust_level in network[curr_id].connections.items():
			if visited[connection_id] == [] and trust_level >= min_trust_level:
				visited[connection_id] = visited[curr_id][:] #using slicing to avoid list aliasing
				visited[connection_id].append(connection_id)
				if common_topics(network[connection_id], topics):
					return visited[connection_id][1:] #slice to exlude sender from path
				else:
					queue.append(connection_id)