from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
# Create your tests here.


class StudentTestCase(LiveServerTestCase):



    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def test_student_find_solos(self):
        home_page = self.browser.get(self.live_server_url +'/')
        brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        self.assertEqual('JMD', brand_element.text)
        self.fail('Incomplete Test')

    def tearDown(self):
        self.browser.quit()
