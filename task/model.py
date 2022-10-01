from pydantic import BaseModel

class Characteristic(BaseModel):
	id: str
	topics: list[str]

class Connection(BaseModel):
	id: str
	trustLevel: int

class Person(BaseModel):
	characteristic: Characteristic
	connections = []
