from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class  SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_to_login(self, username: str, password: str):
        login_element = self.driver.find_element(By.ID, 'login_field')
        login_element.send_keys(username)

        password_element = self.driver.find_element(By.ID, 'password')
        password_element.send_keys(password)

        btn_login = self.driver.find_element(By.NAME, 'commit')
        btn_login.click()
