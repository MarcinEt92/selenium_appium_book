import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


@pytest.fixture()
def maximize_window(driver):
    driver.maximize_window()


@pytest.fixture()
def get_sauce_main_page(driver):
    driver.get("https://www.saucedemo.com/")
