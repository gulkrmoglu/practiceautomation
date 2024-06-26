from practice_automation.pages.constants.globalConstants import *
from practice_automation.pages.PageBase import PageBase
import time

class Register(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver    
       
    def character_register(self):
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(MAIL)
        email.send_keys("piar1.toobeto@gmail.com")
        password=self.WaitForElementVisible(PASSWORD)
        password.send_keys("222367")
        register=self.WaitForElementVisible(REGISTER)
        register.click()
        time.sleep(4)   
        alert_message=self.WaitForElementVisible(ALERT_MESSAGE)
        assert {alert_message.text == ALERTMESSAGE}

    def valid_register(self):
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(MAIL)
        email.send_keys("piar1.toobeto@gmail.com")
        password=self.WaitForElementVisible(PASSWORD)
        password.send_keys("56.R:7bm41")
        register=self.WaitForElementVisible(REGISTER)
        register.click()
        time.sleep(4)

    def invalid_register(self):
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(MAIL)
        email.send_keys("piar1.toobeto@gmail.comm")
        password=self.WaitForElementVisible(PASSWORD)
        password.send_keys("56.R:7bm41")
        register=self.WaitForElementVisible(REGISTER)
        register.click()
        time.sleep(4)
        errormessage=self.WaitForElementVisible(ERRORMESSAGE)
        assert {errormessage.text == ERROR_MESSAGE}

    def empty_email_register(self):
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(MAIL)
        email.send_keys(" ")
        password=self.WaitForElementVisible(PASSWORD)
        password.send_keys("56.R:7bm41")
        register=self.WaitForElementVisible(REGISTER)
        register.click()
        time.sleep(4)
        errormessage=self.WaitForElementVisible(ERRORMESSAGE)
        assert {errormessage.text == ERROR_MESSAGE}

    def empty_password_register(self):
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(MAIL)
        email.send_keys("piar1.toobeto@gmail.com")
        password=self.WaitForElementVisible(PASSWORD)
        password.send_keys("")
        register=self.WaitForElementVisible(REGISTER)
        register.click()
        time.sleep(4)
        passwordalert=self.WaitForElementVisible(PASSWORDALERT)
        assert {passwordalert.text == PASSWORD_ALERT}
    
