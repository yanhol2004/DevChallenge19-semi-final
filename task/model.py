from pydantic import BaseModel

class Person_char(BaseModel):
	id: str
	topics: list[str]

class Person(BaseModel):
	topics: list[str]
	connections = {}

class Message(BaseModel):
	text: str
	topics: list[str]
	from_person_id: str
	min_trust_level: int