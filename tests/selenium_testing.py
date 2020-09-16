"""
  Setting up Functional testing for layout web tool.
"""

import unittest
import urllib

from flask_testing import LiveServerTestCase
from selenium import webdriver

class TestBase(LiveServerTestCase):
  """
  def create_app(self):
    config_name = 'testing'
    app = create_app(config_name)
    app.config.update(
      # Specify the test database
      SQLALCHEMY_DATABASE_URI='',
      # Change the port that the liveserver listens on
      LIVESERVER_PORT=8943
    )
    return app
  """
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