from fastapi import APIRouter, Path
from model import Characteristic, Person, Connection

router = APIRouter()

network = {}

@router.post("/people")
async def add_person(characteristic: Characteristic) -> dict:
	person = Person(characteristic=characteristic)
	network[person.characteristic.id] = person
	return characteristic.dict()

@router.get("/people") 
async def show_network() -> dict:
	return {"network": network}


@router.post("/people/{person_id}/trust_connections")
async def add_trust_connections(connections: dict, person_id: str = Path(..., title="The ID of the given person."), ):
	for item in connections.items():
		temp = Connection(id=item[0], trustLevel=item[1])
		network[person_id].connections.append(temp)

