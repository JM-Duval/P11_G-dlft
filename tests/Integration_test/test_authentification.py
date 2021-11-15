import pytest
from django.urls import reverse
from tests.conftest import client
from server import clubs, create_app


def test_authentification_route(client):

	email = clubs[0]['email']
	data = {'email': email}
	
	response = client.post(reverse('/'), data)
	assert response.status_code == 302

	"""
	response = client.post('showSummary', data={'email': email})
	data = response.data.decode()
	message = 'Summary | GUDLFT Registration'
	assert message in data
	"""