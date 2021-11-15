from server import competitions, clubs, get_max_booking



def test_max_booking_with_min_points(monkeypatch):
	name_club = 'name_club'
	name_competition = 'name_competition'
	monkeypatch.setitem(clubs[0], 'name', name_club)
	monkeypatch.setitem(clubs[0], 'points', 4)
	monkeypatch.setitem(competitions[0], 'name', name_competition)
	monkeypatch.setitem(competitions[0], 'numberOfPlaces', 7)
	assert get_max_booking(name_competition, name_club) == 4

def test_12_places_max_booking(monkeypatch):
	name_club = 'name_club'
	name_competition = 'name_competition'
	monkeypatch.setitem(clubs[0], 'name', name_club)
	monkeypatch.setitem(clubs[0], 'points', 13)
	monkeypatch.setitem(competitions[0], 'name', name_competition)
	monkeypatch.setitem(competitions[0], 'numberOfPlaces', 13)
	assert get_max_booking(name_competition, name_club) == 12