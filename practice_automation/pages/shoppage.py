from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from practice_automation.pages.constants.globalConstants import *


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)  

    def WaitForElementVisible(self,locator,timeout=40):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))   

    def home_page_scroll(self):
        shop=self.WaitForElementVisible(SHOP_LINK)
        shop.click()        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          
    def home_page_shop(self):
        shop=self.WaitForElementVisible(SHOP_LINK)
        shop.click()
       
    def home_page_product_image(self):
        element = self.WaitForElementVisible(ELEMENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        image=self.WaitForElementVisible(IMAGE)
        image.click()