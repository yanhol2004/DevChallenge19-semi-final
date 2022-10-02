from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_create_people():
	response_garry = client.post("api/people", json={
			"id": "Garry",
  			"topics": [
    		"magic", "books"
  			]
		}
	)

	response_hermiona = client.post("api/people", json={
			"id": "Hermiona",
  			"topics": [
    		"magic", "books"
  			]
		}
	)

	response_ron = client.post("api/people", json={
			"id": "Ron",
  			"topics": [
  			]
		}
	)

	response_snape = client.post("api/people", json={
			"id": "Snape",
  			"topics": [
    		"magic", "books"
  			]
		}
	)

	response_voldemort = client.post("api/people", json={
			"id": "Voldemort",
  			"topics": [
    		"magic", "death"
  			]
		}
	)
	assert response_garry.status_code == 201
	assert response_hermiona.status_code == 201
	assert response_voldemort.status_code == 201
	assert response_ron.status_code == 201
	assert response_snape.status_code == 201

def test_create_connections():
	response_garry = client.post("api/people/Garry/trust_connections", json={
			"Hermiona": 10,
			"Ron":10,
			"Snape":6,
			"Voldemort":1
		}
	)

	response_hermiona = client.post("api/people/Hermiona/trust_connections", json={
			"Garry": 10,
			"Ron":10,
			"Snape":4,
			"Voldemort":1
		}
	)

	response_ron = client.post("api/people/Ron/trust_connections", json={
			"Garry": 10,
			"Hermiona":10,
			"Snape":4,
			"Voldemort":1
		}
	)

	response_snape = client.post("api/people/Snape/trust_connections", json={
			"Garry": 6,
			"Hermiona":6,
			"Ron":4,
			"Voldemort":10
		}
	)

	response_voldemort = client.post("api/people/Voldemort/trust_connections", json={
			"Garry": 3,
			"Hermiona":3,
			"Ron":4,
			"Snape":10
		}
	)
	assert response_garry.status_code == 201
	assert response_hermiona.status_code == 201
	assert response_voldemort.status_code == 201
	assert response_ron.status_code == 201
	assert response_snape.status_code == 201

def test_message():
	response_message = client.post("api/messages", json=
		{
			"text": "Voldemort is alive",
			"topics": [
			],
			"from_person_id": "Garry",
			"min_trust_level": 5
		}
	)
	assert response_message.status_code == 201
	assert response_message.json() == {
		"Garry": ["Hermiona", "Ron", "Snape"],
		"Snape": ["Voldemort"]
	}

def test_path():
	response_path = client.post("api/path", json=
		{
			"text": "Voldemort is alive",
			"topics": [
			    "magic"
			],
			"from_person_id": "Garry",
			"min_trust_level": 5
		}
	)

	assert response_path.json() == {
		"from": "Garry",
		"path": ["Hermiona"]
	} or response_path.json() == {
		"from": "Garry",
		"path": ["Snape"]
	}
