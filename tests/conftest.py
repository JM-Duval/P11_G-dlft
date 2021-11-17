import pytest
from server import create_app, clubs, competitions


@pytest.fixture
def client():
	app = create_app({"TESTING": True})
	with app.test_client() as client:
		yield client


@pytest.fixture
def data_test(monkeypatch):

    club = clubs[0]
    competition = competitions[0]
    
    club_test = \
        {
            'name':'club_test', 
            'points':20, 
            'email':'email@club.com'
        }

    competition_test = \
        {
            'name':'competition_test', 
            'date': "2022-03-27 10:00:00", 
            'numberOfPlaces': 20
        }
    
    monkeypatch.setitem(club, 'name', club_test['name'])
    monkeypatch.setitem(club, 'points', club_test['points'])
    monkeypatch.setitem(club, 'email', club_test['email'])

    monkeypatch.setitem(competition, 'name', competition_test['name'])
    monkeypatch.setitem(competition, 'date', competition_test['date'])
    monkeypatch.setitem(competition, 'numberOfPlaces', 
        competition_test['numberOfPlaces'])

    return club, competition