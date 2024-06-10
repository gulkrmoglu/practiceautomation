from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from practice_automation.pages.shoppage import ShopPage
from practice_automation.pages.constants.globalConstants import *

options = Options()
options.add_argument("start-maximized")

class TestShopPage:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()

    def test_shop_page(self):
        self.shop_page = ShopPage(self.driver)
        self.shop_page.shop_scroll()
        self.shop_page.shop()
        self.shop_page.shop_product_image()
        self.shop_page.shop_android()
        self.shop_page.shop_html()
        self.shop_page.shop_javascript()
        self.shop_page.shop_selenium()