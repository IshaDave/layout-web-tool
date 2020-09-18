"""
  Setting up Functional testing for layout web tool.
"""

import unittest
import urllib

from flask import Flask
from flask_testing import LiveServerTestCase
from selenium import webdriver

class TestBase(LiveServerTestCase):

  def create_app(self):
      app = Flask(__name__)
      app.config['TESTING'] = True
      # Default port is 5000
      app.config['LIVESERVER_PORT'] = 8943
      # Default timeout is 5 seconds
      app.config['LIVESERVER_TIMEOUT'] = 10
      return app

  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_Start(self):
    driver = self.driver
    driver.get('https://in-toto.engineering.nyu.edu/')

    start = driver.find_element_by_xpath('/html/body/div[3]/div/div/a')
    start.click()

    self.driver.quit()

if __name__ == '__main__':
    unittest.main()
