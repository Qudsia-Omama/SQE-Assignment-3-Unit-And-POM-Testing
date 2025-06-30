import unittest
import time
from POMProjectDemo.Pages.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.tutorialspoint.com/selenium/practice/login.php#")
        login=LoginPage(driver)
        login.enter_email("qudsiaomama@gmail.com")
        login.enter_password("12345678")
        login.click_login()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed By Qudsia")

if __name__ == '__main__':
    unittest.main()
