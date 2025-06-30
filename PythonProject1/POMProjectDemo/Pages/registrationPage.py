from selenium.webdriver.common.by import By

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.firstname_id = "firstname"
        self.lastname_id = "lastname"
        self.username_id = "username"
        self.password_id = "password"
        self.register_button_class = "btn-primary"

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname_id).clear()
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_id).clear()
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_register(self):
        self.driver.find_element(By.CLASS_NAME, self.register_button_class).click()
