from practice_automation.pages.constants.globalConstants import *
from practice_automation.pages.PageBase import PageBase

class ShopPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def shop_scroll(self):
        shop=self.WaitForElementVisible(SHOP_LINK)
        shop.click()        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          
    def shop(self):
        shop=self.WaitForElementVisible(SHOP_LINK)
        shop.click()
       
    def shop_product_image(self):
        element = self.WaitForElementVisible(ELEMENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        image=self.WaitForElementVisible(IMAGE)
        image.click()
        
    def shop_android(self):
        self.shop()
        android=self.WaitForElementVisible(ANDROID)
        android.click()
        image_android=self.WaitForElementVisible(IMAGE_ANDROID)
        image_android.click()

    def shop_html(self):
        self.shop()
        html=self.WaitForElementVisible(HTML)
        html.click()
        image_html=self.WaitForElementVisible(IMAGE_HTML)
        image_html.click()

    def shop_javascript(self):
        self.shop()
        javascript=self.WaitForElementVisible(JAVASCRIPT)
        javascript.click()
        image_javascript=self.WaitForElementVisible(IMAGE_JAVASCRIPT)
        image_javascript.click()

    def shop_selenium(self):
        self.shop()           
        selenium=self.WaitForElementVisible(SELENIUM)
        selenium.click()
        image_selenium=self.WaitForElementVisible(IMAGE_SELENIUM)
        image_selenium.click()

    


        



