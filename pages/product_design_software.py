from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import MainPage
from selenium.webdriver.common.by import By
from utils.test_data import text_empty_cart

from utils.test_data import page_title_name_design


class DesignSoftware(MainPage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def check_page_title(self):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h1').text
        assert page_title == page_title_name_design

    def buy_two_product(self):
        plus = self.driver.find_element(By.CSS_SELECTOR, '.fa.fa-plus')
        plus.click()

        btn_add_to_cart = self.driver.find_element(By.CSS_SELECTOR, '#add_to_cart')
        btn_add_to_cart.click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".fa.fa-shopping-cart.fa-stack + sup"), "2"))
        my_cart = self.driver.find_element(By.CSS_SELECTOR, '.fa.fa-shopping-cart.fa-stack')
        my_cart.click()

        product = self.driver.find_element(By.CSS_SELECTOR, 'h6').text
        count = self.driver.find_element(By.CSS_SELECTOR, '[value="2"]')

        assert product == page_title_name_design
        assert count.get_attribute('value') == '2'

    def delete_buy(self):
        minus = self.driver.find_element(By.CSS_SELECTOR, '[title="Remove one"]')
        minus.click()

        minus = self.driver.find_element(By.CSS_SELECTOR, '[title="Remove one"]')
        minus.click()

        cart_message = self.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]').text
        assert text_empty_cart in cart_message
