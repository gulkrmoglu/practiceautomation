from practice_automation.pages.constants.globalConstants import *
from practice_automation.pages.PageBase import PageBase
import time

class Login(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver    

    def valid_login(self):
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(LOGIN_EMAIL)
        email.send_keys("piar1.toobeto@gmail.com")
        password=self.WaitForElementVisible(LOGIN_PASSWORD)
        password.send_keys("56.R:7bm41")
        login=self.WaitForElementVisible(LOGIN)
        login.click()
        logout=self.WaitForElementVisible(LOGOUT)
        logout.click()
        message_login=self.WaitForElementVisible(MESSAGELOGIN)
        message_login.click()
        assert {message_login.text == MESSAGE_LOGIN}
        

    def invalid_login(self):    
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(LOGIN_EMAIL)
        email.send_keys("tomsmith")
        password=self.WaitForElementVisible(LOGIN_PASSWORD)
        password.send_keys("453423")
        login=self.WaitForElementVisible(LOGIN)
        login.click()
        alert_null_login=self.WaitForElementVisible(ALERTINVALIDOGIN)
        alert_null_login.click()
        assert {alert_null_login.text == ALERT_INVALID_LOGIN}

    def null_login_password(self):    
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(LOGIN_EMAIL)
        email.send_keys("piar1.toobeto@gmail.com")
        password=self.WaitForElementVisible(LOGIN_PASSWORD)
        password.send_keys(" ")
        login=self.WaitForElementVisible(LOGIN)
        login.click()
        alert_null_password=self.WaitForElementVisible(ALERTNULLPASSWORD)
        alert_null_password.click()
        assert {alert_null_password.text == ALERT_NULL_PASSWORD}  

    def null_login_email(self):    
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(LOGIN_EMAIL)
        email.send_keys(" ")
        password=self.WaitForElementVisible(LOGIN_PASSWORD)
        password.send_keys("56.R:7bm41")
        login=self.WaitForElementVisible(LOGIN)
        login.click()
        alert_null_email=self.WaitForElementVisible(ALERTNULLEMAIL)
        assert {alert_null_email.text == ALERT_NULL_EMAIL}  

    def null_login(self):    
        account=self.WaitForElementVisible(ACCOUNT)
        account.click()
        email=self.WaitForElementVisible(LOGIN_EMAIL)
        email.send_keys(" ")
        password=self.WaitForElementVisible(LOGIN_PASSWORD)
        password.send_keys(" ")
        login=self.WaitForElementVisible(LOGIN)
        login.click()
        alert_null_login=self.WaitForElementVisible(ALERTNULLLOGIN)
        alert_null_login.click()
        assert { alert_null_login.text == ALERT_NULL_LOGIN} 
         
