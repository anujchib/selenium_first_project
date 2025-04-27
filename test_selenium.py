# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# print(driver.title)
# time.sleep(5)
# driver.quit()
import unittest
from selenium import webdriver
import time

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Setup: Initialize the WebDriver (Chrome)
        self.driver = webdriver.Chrome()

    def test_google_title(self):
        # Test: Check the title of Google homepage
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)  # This will pass if "Google" is in the title.

    def tearDown(self):
        # Cleanup: Quit the WebDriver after the test
        time.sleep(5)  # Optionally wait before closing the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()  # This runs the test case.

