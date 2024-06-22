from selenium import webdriver
import pytest
from practice_automation.pages.register import Register
from practice_automation.pages.constants.globalConstants import *

@pytest.mark.usefixtures("setup")
class TestRegister:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.register = Register(self.driver)

    def test_register(self):        
        self.register.character_register()
        self.register.valid_register()
        self.register.invalid_register()
        self.register.empty_email_register()
        self.register.empty_password_register()

