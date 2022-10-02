from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_create_people():
	response_garry = client.post("/people", json={
			"id": "Garry",
  			"topics": [
    		"magic", "books"
  			]
		}
	)

	response_hermiona = client.post("/people", json={
			"id": "Hermiona",
  			"topics": [
    		"magic", "books"
  			]
		}
	)

	response_ron = client.post("/people", json={
			"id": "Ron",
  			"topics": [
    		
  			]
		}
	)

	response_snape = client.post("/people", json={
			"id": "Snape",
  			"topics": [
    		"magic", "books"
  			]
		}
	)

	response_voldemort = client.post("/people", json={
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
	response_garry = client.post("/people/Garry/trust_connections", json={
			"Hermiona": 10,
			"Ron":10,
			"Snape":6,
			"Voldemort":1
		}
	)

	response_hermiona = client.post("/people/Hermiona/trust_connections", json={
			"Garry": 10,
			"Ron":10,
			"Snape":4,
			"Voldemort":1
		}
	)

	response_ron = client.post("/people/Ron/trust_connections", json={
			"Garry": 10,
			"Hermiona":10,
			"Snape":4,
			"Voldemort":1
		}
	)

	response_snape = client.post("/people/Snape/trust_connections", json={
			"Garry": 6,
			"Hermiona":6,
			"Ron":4,
			"Voldemort":10
		}
	)

	response_voldemort = client.post("/people/Voldemort/trust_connections", json={
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
	response_message = client.post("/messages", json=
		{
			"text": "Voldemort is alive",
			"topics": [
			    "magic"
			],
			"from_person_id": "Garry",
			"min_trust_level": 5
		}
	)
	assert response_message.status_code == 201
	assert response_message.json() == {
		"Garry": ["Hermiona", "Snape"],
		"Snape": ["Voldemort"]
	}


