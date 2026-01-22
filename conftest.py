from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    chrome_driver = webdriver.chrome
    yield chrome_driver
