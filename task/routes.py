from fastapi import APIRouter, Path, HTTPException
from model import PersonCreateRequest, Person, Message
from search_algorithms import search_receivers, search_shortest_path

router = APIRouter()

network = {}


@router.post("/people", status_code=201)
async def add_person(person_attributes: PersonCreateRequest) -> dict:
    if person_attributes.id in network:
        raise HTTPException(status_code=422, detail="Such a person already exists")
    person = Person(topics=person_attributes.topics)
    network[person_attributes.id] = person
    return person_attributes.dict()

@router.post("/people/{person_id}/trust_connections", status_code=201)
async def add_trust_connections(connections: dict, person_id: str = Path(..., title="The ID of the given person."), ):
    if person_id not in network:
        raise HTTPException(status_code=404, detail="Person with provided ID does not exist")
    for connection_id, connection_trust in connections.items():
        if connection_id not in network:
            raise HTTPException(status_code=422, detail="Cannot establish connection with non existent person")
        if not isinstance(connection_trust, int) or connection_trust > 10 or connection_trust < 1:
            raise HTTPException(status_code=422, detail="Invalid trust level value")
        network[person_id].connections[connection_id] = connection_trust


@router.post("/messages", status_code=201)
async def send_message(message: Message) -> dict:
    return search_receivers(network, message)


@router.post("/path", status_code=201)
async def find_shortest_path(message: Message) -> dict:
    return {"from": message.from_person_id,
            "path": search_shortest_path(network, message)
            }

