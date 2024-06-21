from selenium import webdriver
import pytest
from practice_automation.pages.shoppage import ShopPage
from practice_automation.pages.constants.globalConstants import *

@pytest.mark.usefixtures("setup")
class TestShopPage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.shop_page = ShopPage(self.driver)

    def test_shop_page(self):
        self.shop_page.shop_scroll()
        self.shop_page.shop()
        self.shop_page.shop_product_image()
        self.shop_page.shop_android()
        self.shop_page.shop_html()
        self.shop_page.shop_javascript()
        self.shop_page.shop_selenium()