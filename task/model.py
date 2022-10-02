from pydantic import BaseModel

class Person_char(BaseModel):
	id: str
	topics: list[str]

class Person(BaseModel):
	topics: list[str]
	connections = {}
