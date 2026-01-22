from time import sleep
from selenium import webdriver
import pytest

from pages.cart_page import CartPage
from pages.category_desks import CategoryDesks

from pages.product_design_software import DesignSoftware


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(7)
    yield chrome_driver
    sleep(3)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def category_desks(driver):
    return CategoryDesks(driver)


@pytest.fixture()
def product_design_software(driver):
    return DesignSoftware(driver)
