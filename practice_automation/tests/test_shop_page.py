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

    def test_home_page(self):
        self.home_page = ShopPage(self.driver)
        self.home_page.home_page_scroll()
        self.home_page.home_page_shop()
        self.home_page.home_page_product_image()