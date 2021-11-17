import server
from tests.conftest import client
from server import clubs, create_app


def test_login_with_right_email(client):
	email = clubs[0]['email']
	response = client.post('showSummary', data={'email': email})
	data = response.data.decode()
	message_summary_menu = 'Summary | GUDLFT Registration'
	assert message_summary_menu in data


def test_login_with_wrong_email(client):
	wrong_email = 'wrong@email.com'
	response = client.post('showSummary', data={'email': wrong_email})
	data = response.data.decode()
	message_welcome_menu = 'GUDLFT Registration'
	assert message_welcome_menu in data