from collections import deque
from model import Message


def has_all_topics(person, topics):  # checking if person has all the topics listed in message
    return topics.issubset(person.topics)


# searching for receivers with breadth-first search. Consider network as an oriented graph,
# where each person is a node, and their trust connections are edges
def search_receivers(network, message: Message):
    receivers = {}  # from_person: [to_persons]
    # using set instead of list to check key presence for O(1)
    visited = set()  # contains visited nodes to avoid spamming
    # implementing queue with deque class
    people_queue = deque()  # contains nodes to visit

    people_queue.append(message.from_person_id)  # selecting sender as starting node
    visited.add(message.from_person_id)
    while people_queue:  # while queue is not empty
        current_person_id = people_queue.popleft()
        # iterating through all connections, searching for eligible receiver
        for connection_id, trust_level in network[current_person_id].connections.items():
            if connection_id not in visited and trust_level >= message.min_trust_level and has_all_topics(
                    network[connection_id], message.topics):
                # if it is first time person sends message, we create empty entry in dict
                if current_person_id not in receivers:
                    receivers[current_person_id] = []
                receivers[current_person_id].append(connection_id)
                people_queue.append(connection_id)  # adding to queue to check friends of this person
                visited.add(connection_id)
    return receivers


# searching for shortest path with breadth-first search
# first node after sender to have all message's topics is the closest receiver
# path to the closest receiver is the shortest path that we need to find
def search_shortest_path(network, message):
    # dictionary of all visited nodes with last visited node to restore path and to avoid spamming
    visited = {}  # last visited node as value, id as key
    queue = deque()  # nodes to visit

    queue.append(message.from_person_id)  # selecting starting node
    visited[message.from_person_id] = message.from_person_id
    while queue:  # while queue is not empty
        current_person_id = queue.popleft()
        # iterating through all connection of current node
        for connection_id, trust_level in network[current_person_id].connections.items():
            if connection_id not in visited and trust_level >= message.min_trust_level:
                visited[connection_id] = current_person_id
                # if connected person has required topics it is receiver that we were searching for
                if has_all_topics(network[connection_id], message.topics):
                    return restore_path(visited, message.from_person_id, connection_id)
                else:
                    queue.append(connection_id)
    return []  # if there wasn't anyone eligible to receive message


# going back from receiver of message to sender to restore path
def restore_path(visited: dict, sender, receiver):
    path = [receiver]
    while path[-1] != sender:
        path.append(visited[path[-1]])
    path.reverse()
    return path[1:]
