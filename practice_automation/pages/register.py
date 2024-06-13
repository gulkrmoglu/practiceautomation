from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from practice_automation.pages.constants.globalConstants import *
import time

class Register:

    def __init__(self, driver):
        self.driver = driver

    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)  

    def WaitForElementVisible(self,locator,timeout=40):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))   
    
    
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
    
