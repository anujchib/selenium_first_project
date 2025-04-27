# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# print(driver.title)
# time.sleep(5)
# driver.quit()
# import unittest
# from selenium import webdriver
# import time

# class GoogleTest(unittest.TestCase):
#     def setUp(self):
#         # Setup: Initialize the WebDriver (Chrome)
#         self.driver = webdriver.Chrome()

#     def test_google_title(self):
#         # Test: Check the title of Google homepage
#         self.driver.get("https://www.google.com")
#         self.assertIn("Google", self.driver.title)  # This will pass if "Google" is in the title.

#     def tearDown(self):
#         # Cleanup: Quit the WebDriver after the test
#         time.sleep(5)  # Optionally wait before closing the browser
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()  # This runs the test case.

import unittest
from selenium import webdriver
import time
from extentreports import ExtentReports, ExtentTest, LogStatus

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Setup: Initialize ExtentReports and the WebDriver (Chrome)
        self.driver = webdriver.Chrome()
        self.extent = ExtentReports("test-output/ExtentReports.html", True)
        self.test = self.extent.startTest("Test Google", "Testing Google home page")

    def test_google_title(self):
        # Test: Check the title of Google homepage
        self.driver.get("https://www.google.com")
        self.test.log(LogStatus.INFO, "Opened Google")
        self.assertIn("Google", self.driver.title)  # This will pass if "Google" is in the title.
        self.test.log(LogStatus.PASS, "Title verified")

    def tearDown(self):
        # Cleanup: Quit the WebDriver after the test
        time.sleep(5)  # Optionally wait before closing the browser
        self.driver.quit()
        self.extent.endTest(self.test)
        self.extent.flush()

if __name__ == "__main__":
    unittest.main()  # This runs the test case.


