from server import clubs, competitions, get_active_competition
from datetime import date, datetime, timedelta


today = datetime.now()


def test_active_competition_with_past_date(monkeypatch):
	#date_test = today - timedelta(days=1)
	date_test = '2020-11-12 17:30:00'
	monkeypatch.setitem(competitions[0], 'date', date_test)
	active_competitions = get_active_competition()
	date_competitions = []
	for competition in active_competitions:
		date_competitions.append(competition['date'])
	assert date_test not in date_competitions


def test_active_competition_with_past_date(monkeypatch):
	#date_test = today + timedelta(days=1)
	date_test = '2022-11-12 17:30:00'
	monkeypatch.setitem(competitions[0], 'date', date_test)
	active_competitions = get_active_competition()
	date_competitions = []
	for competition in active_competitions:
		date_competitions.append(competition['date'])
	assert date_test in date_competitions



