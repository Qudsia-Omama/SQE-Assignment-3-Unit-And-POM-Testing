import unittest
import time
from POMProjectDemo.Pages.registrationPage import RegistrationPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_register_valid(self):
        driver = self.driver
        driver.get("https://www.tutorialspoint.com/selenium/practice/register.php#")
        register = RegistrationPage(driver)
        register.enter_firstname("Qudsia")
        register.enter_lastname("Omama")
        register.enter_username("Qudsia002")
        register.enter_password("12345678")
        register.click_register()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed By Qudsia")

if __name__ == '__main__':
    unittest.main()

