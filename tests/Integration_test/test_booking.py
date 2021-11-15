import server
import requests
from tests.conftest import client
from server import competitions, clubs, create_app, get_active_competition,\
	               get_max_booking
from bs4 import BeautifulSoup

import re


class TestBooking:


	def get_points_club_available(self, club, data):
		soup = BeautifulSoup(data, "html.parser")
		name_club = club['name']
		selection = soup.body.find(text=re.compile(name_club))\
					.replace(" ", "").replace("/n", "")
		start_word = 'Total'
		final_word = 'points'
		start_of_selection = selection.find(start_word) + len(start_word) + 1
		end_of_selection = selection.find(final_word)
		result = int(selection[start_of_selection:end_of_selection])
		return result

	def get_numberOfPlaces_competition_available(self, competition, data):
		soup = BeautifulSoup(data, "html.parser")
		name_competition = competition['name']
		selection = soup.body.find(text=re.compile(name_competition))\
					.parent.text
		start_word = 'Number of Places'
		start_of_selection = selection.find(start_word) + len(start_word) + 1
		result = int(selection[start_of_selection:])
		return result

	def test_booking_points_club(self, client, monkeypatch):
		club = clubs[0]
		points_club = 20
		monkeypatch.setitem(club, 'points', points_club)
		competition = competitions[0]
		places = 10
		response = client.post('/purchasePlaces',
			data={'club': club['name'], 'competition': competition['name'], 
			'places': places})
		data = response.data.decode()
		result_points_club = self.get_points_club_available(club, data)
		assert result_points_club == points_club - places

	def test_booking_places_competition(self, client, monkeypatch):
		club = clubs[0]
		competition = competitions[0]
		places_competition = 30
		monkeypatch.setitem(competition, 'numberOfPlaces', places_competition)
		places = 10
		response = client.post('/purchasePlaces',
			data={'club': club['name'], 'competition': competition['name'], 
			'places': places})
		data = response.data.decode()
		result_places_competition = \
			self.get_numberOfPlaces_competition_available(competition, data)
		assert result_places_competition == places_competition - places
