from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from server import clubs, competitions

import time


class TestUserRoute(StaticLiveServerTestCase):
    
    """Testing of the folling features: login, booking places, logout"""

    def setUp(self):
        self.browser = webdriver.Chrome('tests/Fonctionnal_test/chromedriver')
        self.live_server_url = "http://127.0.0.1:5000/"
        self.name_club = clubs[0]['name']
        self.email_club = clubs[0]['email']
        self.name_competition = competitions[0]['name']
        self.message_welcome_menu = 'Welcome, ' + self.email_club
        self.message_index_menu = 'Welcome to the GUDLFT Registration Portal!'
        

    def signup(self):
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.find_element_by_tag_name('h1').text, 
            self.message_index_menu)
        time.sleep(2)
        femail = self.browser.find_element_by_name('email')
        femail.send_keys(self.email_club)
        agree_term = self.browser.find_element_by_xpath('//button')
        agree_term.click()
        time.sleep(2)
        #message_welcome_menu = 'Welcome, ' + self.email_club
        self.assertEqual(self.browser.find_element_by_tag_name('h2').text, 
            self.message_welcome_menu)
        #print(self.browser.current_url)
    
    def booking_places(self):
        agree_term = self.browser.find_element_by_link_text('Book Places')
        agree_term.click()
        time.sleep(2)
        places = 3 
        nb_places = self.browser.find_element_by_name('places')
        nb_places.send_keys(places)
        time.sleep(2)
        agree_term_2 =self.browser.find_element_by_xpath('//button')
        agree_term_2.click()
        time.sleep(2)
        self.assertEqual(self.browser.find_element_by_tag_name('h2').text, 
            self.message_welcome_menu)

    def logout(self):
        agree_term = self.browser.find_element_by_link_text('Logout')
        agree_term.click()
        self.assertEqual(self.browser.find_element_by_tag_name('h1').text, 
            self.message_index_menu)
        time.sleep(2)
        
    def closeDown(self):
        self.browser.close()
    
    def test_run(self):
        self.signup()
        self.booking_places()
        self.logout()
        self.closeDown()
