from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://practice.automationtesting.in/")
        yield 
        request.cls.driver=driver
        driver.quit()