from pydantic import BaseModel


# model used to receive data on the /api/people endpoint
class PersonCreateRequest(BaseModel):
    id: str
    topics: set


# model listing all attributes except id
# used to store people in network dictionary
class Person(BaseModel):
    topics: set
    connections = {}


# model to receive data on the /api/message and /api/path endpoints
class Message(BaseModel):
    text: str
    topics: set
    from_person_id: str
    min_trust_level: int
