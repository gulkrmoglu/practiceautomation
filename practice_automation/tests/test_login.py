from selenium import webdriver
import pytest
from practice_automation.pages.login import Login
from practice_automation.pages.constants.globalConstants import *

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = Login(self.driver)

    def test_register(self):        
        self.login.valid_login()
        self.login.invalid_login()
        self.login.null_login_password()
        self.login.null_login_email()
        self.login.null_login()
        