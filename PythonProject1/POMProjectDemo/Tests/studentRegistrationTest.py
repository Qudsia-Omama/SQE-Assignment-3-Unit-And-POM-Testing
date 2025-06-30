import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestStudentRegistrationForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_fill_form(self):
        driver = self.driver
        driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        driver.find_element(By.ID, "name").send_keys("Qudsia Omama")
        driver.find_element(By.ID, "email").send_keys("qudsiaomama@gmail.com")
        driver.find_element(By.XPATH, "//label[text()='Female']/preceding-sibling::input").click()
        driver.find_element(By.ID, "mobile").send_keys("03001234567")
        driver.find_element(By.ID, "dob").send_keys("2004-05-30")
        driver.find_element(By.ID, "subjects").send_keys("Software Engineering")
        driver.find_elements(By.ID, "hobbies")[0].click()
        driver.find_element(By.ID, "picture").send_keys(r"C:\Users\huawei\Pictures\Screenshots\1.png")
        (driver.find_element(By.XPATH, "//textarea[@placeholder='Currend Address']").send_keys
         ("Karachi, Pakistan"))
        Select(driver.find_element(By.ID, "state")).select_by_visible_text("Haryana")
        Select(driver.find_element(By.ID, "city")).select_by_visible_text("Agra")

        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)
        submit_button.click()

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed By Qudsia")

if __name__ == "__main__":
    unittest.main()


