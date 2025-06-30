from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_id = "email"
        self.password_id = "password"
        self.login_button_class = "btn-primary"

    def enter_email(self,email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID,self.email_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button_class).click()
