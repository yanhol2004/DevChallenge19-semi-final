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
		for connection in network[curr_id].connections.items():
			connection_id = connection[0]
			trust_level = connection[1]
			if not visited[connection_id] and trust_level >= min_trust_level and common_topics(network[connection_id], topics):	
				if curr_id not in receivers:
					receivers[curr_id] = []
				receivers[curr_id].append(connection_id)
				queue.append(connection_id)
				visited[connection_id] = True
	return receivers
