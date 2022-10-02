from fastapi import APIRouter, Path, HTTPException, status
from model import Person_char, Person, Message
from bfs import bfs_of_receivers, bfs_shortest_path

router = APIRouter()

network = {}

@router.post("/people", status_code=201)
async def add_person(characteristic: Person_char) -> dict:
	if network.__contains__(characteristic.id):
		raise HTTPException(status_code=422, detail="Such a person already exists")
		return
	person = Person(topics = characteristic.topics)
	network[characteristic.id] = person
	return characteristic.dict()

@router.get("/people", status_code=201)
async def show_network() -> dict:
	return {"network": network}


@router.post("/people/{person_id}/trust_connections",status_code=201)
async def add_trust_connections(connections: dict, person_id: str = Path(..., title="The ID of the given person."), ):
	if not network.__contains__(person_id):
		raise HTTPException(status_code=404, detail="Person with provided ID does not exist")
		return
	for item in connections.items():
		connection_id = item[0]
		connection_trust = item[1]
		if not network.__contains__(connection_id):
			raise HTTPException(status_code=422, detail="Cannot establish connection with non existent person")
			return
		if connection_trust > 10 or connection_trust < 1:
			raise HTTPException(status_code=422, detail="Invalid trust level value")
		network[person_id].connections[connection_id] = connection_trust

@router.post("/messages", status_code=201)
async def send_message(message: Message) -> dict:
	return bfs_of_receivers(network, message.topics, message.from_person_id, message.min_trust_level)

@router.post("/path", status_code=201)
async def find_shortest_path(message: Message) -> dict:
	return {"from": message.from_person_id,
			"path": bfs_shortest_path(network, message.topics, message.from_person_id, message.min_trust_level)
			}