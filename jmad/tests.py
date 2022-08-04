from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create your tests here.


class StudentTestCase(LiveServerTestCase):



    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def test_student_find_solos(self):
        home_page = self.browser.get(self.live_server_url +'/')
        # brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        brand_element = self.browser.find_element(By.CLASS_NAME,'navbar-brand')
        self.assertEqual('JMD', brand_element.text)


        instrument_input = self.browser.find_element(By.ID,'input#jmad-instrument')
        self.assertEqual(instrument_input.get_attribute('placeholder'),'i.e. trumpet')
        artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-artist"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'),'i.e. Davis')
        instrument_input.send_keys('saxophone').submit()
        self.fail('Incomplete Test')

    

    def tearDown(self):
        self.browser.quit()
