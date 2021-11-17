import pytest
from flask import url_for
#from django.urls import reverse
from tests.conftest import client, data_test
from server import create_app
from bs4 import BeautifulSoup
import re


class noTestUserRoute:
    """
    Fonctionnal test including authentification, booking places and logout
    """
    
    def setup_method(self):
        self.club = data_test[0]
        self.competition = data_test[1]


    def test_login_route(self, client):
        response = client.post('showSummary', 
        data={'email': club['email']})
        assert response.status_code == 200

    def test_booking_places(self, client):
        places = 10
        response = client.post('/purchasePlaces',
            data={'club': club['name'], 'competition': competition['name'], 
            'places': places})
        assert response.status_code == 200


def test_user_route(client, data_test):
    
    club = data_test[0]
    competition = data_test[1]
       
    # // login //
    response = client.post('showSummary', 
        data={'email': club['email']})
    assert response.status_code == 200


    # // booking places //
    places = 10
    response_book_places = client.post('/purchasePlaces',
        data={'club': club['name'], 'competition': competition['name'], 
        'places': places})
    assert response_book_places.status_code == 200

    places = 15
    response_book_places = client.post('/purchasePlaces',
        data={'club': club['name'], 'competition': competition['name'], 
        'places': places})
    data = response_book_places.data.decode()
    assert response_book_places.status_code == 200

    # // come back to welcome menu //
    response_back_welcome_menu = client.get(url_for('book',competition=competition['name'],club=club['name']))
    data = response_back_welcome_menu.data.decode()
    soup = BeautifulSoup(data, "html.parser")
    selection = soup.body.find(text=re.compile('Places available:'))\
                    .replace(" ", "").replace("/n", "")
    start_word = 'Placesavailable:'
    final_word = 'Réservationpossible:'
    start_of_selection = selection.find(start_word) + len(start_word)
    end_of_selection = selection.find(final_word)
    result = int(selection[start_of_selection:end_of_selection])
    assert club['points'] == result

    # // logout //
    response_logout = client.get(url_for('logout'))
    assert response_logout.status_code == 302
    