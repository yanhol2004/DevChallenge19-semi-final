# DevChallenge XIX semi-final round
This repository contains my submission for the DevChallenge semi-final round, where I secured absolute 2nd place after this round. You can find the task description [here](https://docs.google.com/document/d/1fJcMrI3MQEze8QWbnL3ltiIR9_W1ShdL7KoFXUFNjpE/edit).

Below are the instructions to run the code, along with an explanation of my algorithm and the reasoning behind specific design choices.

## Short summary of the task
The task was to develop a REST API for a trust network, where people can assign trust levels to each other based on shared expertise topics. The API allows creating and updating trust connections between people and facilitates sending messages. Messages are delivered based on trust levels and shared expertise topics. There are two types of message delivery: broadcast, where messages are sent to all contacts, and non-broadcast, where messages follow a path through trusted individuals to a final recipient with the required expertise. Responses track the message delivery path.

## Short explanation of the solution
I implemented the solution using following libraries: FastAPI, uvicorn for the server, and Pydantic for data validation. The API manages people and trust connections stored in a dictionary, with expertise topics stored in sets for fast lookups. For message delivery, I used a breadth-first search (BFS) algorithm with a deque for optimal performance, ensuring O(V + E) complexity. In the /api/path endpoint, BFS is used to find the shortest path to a recipient based on trust levels. Tests were written using pytest to ensure correct functionality.

## How to run application
To start the service in the directory with the docker-compose file, execute the terminal command 
  ```
  docker-compose up
  ```
## Implementation comments
- Endpoints "/api/people" and "/api/{id}/trust_connections" are implemented straightforwardly, just writing data
into dictionary "network", where all persons' attributes are stored as a value, and person id is a key.
- Topics of people and messages are saved in a set data structure to allow checking that person has all required
topics faster.

- For endpoint "/api/messages," breadth-first search algorithm is used to traverse through the dictionary "network", which we consider as a graph.
- To maximize efficiency set data structure is used to mark visited nodes. This allows checking if node of the graph
was visited with O(1) time complexity.
- To allow enqueue and dequeue items with O(1) complexity, deque was used (instead of a more obvious option
as queue from python module Queue, which indeed has lower efficiency).
- Therefore, the general complexity of implemented BFS is O(V + E), where V - all vertices(number of people in the network), and E - all edges(number of trust_connections between people)

- For endpoint "/api/path" BFS was implemented as well. To mark visited nodes and later backtrack the path, we use
the dictionary 'visited' that has all visited nodes as the keys and stores parent nodes (from which we accessed
node in the key) as values.
- As BFS is traversing layerwise, it is obvious that the first node with all required
topics is the closest receiver, the path to which is the shortest. To restore the path, we use the 'visited' dictionary, moving backward from the receiver of the message to the sender.

## Possible improvements
To make the service better, we may add more endpoints to increase functionality, to adapt the program for large data, it could be connected to a database. Additionaly, to respond more efficiently for similar requests, we can cache obtained results. Also, to generally improve performance, we may pick a more efficient algorithm for search, along with faster data structures suitable for the algorithm.
