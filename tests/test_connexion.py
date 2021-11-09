import server
#from server import create_app
from tests.conftest import client
from server import loadClubs

clubs = loadClubs()

def test_acces_showSummary_with_right_email(client):
	email = clubs[0]['email']
	response = client.post('/showSummary', data={'email': email})
	assert response.status_code == 200
	

def test_acces_showSummary_with_wrong_email(client):
	wrong_email = 'wrong@email.com'
	response = client.post('/showSummary', data={'email': wrong_email})
	data = response.data.decode()
	#print(data)
	#print(response.request.get_json())
	assert response.status_code == 200
