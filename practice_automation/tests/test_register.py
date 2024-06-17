from selenium import webdriver
import pytest
from practice_automation.pages.register import Register
from practice_automation.pages.constants.globalConstants import *


class TestRegister:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()

    def test_register(self):
        self.register = Register(self.driver)
        self.register.character_register()
        self.register.valid_register()
        self.register.invalid_register()
        self.register.empty_email_register()
        self.register.empty_password_register()
