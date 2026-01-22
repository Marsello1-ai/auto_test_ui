from selenium.webdriver.common.by import By
from pages.base_page import MainPage
from utils.test_data import text_empty_cart, value_number_cart


class CartPage(MainPage):
    page_url = '/shop/cart'

    def empty_cart(self):
        product_in_cart = self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-shopping-cart fa-stack"] + sup').text
        if product_in_cart == '':
            cart_message = self.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]').text
            assert text_empty_cart in cart_message
        else:
            print('В корзине есть товары')

    def check_number(self):
        number = self.driver.find_element(By.TAG_NAME, 'small').text
        assert number == value_number_cart

    def check_contact(self):
        contact_text = 'Contact Us'
        contact = self.driver.find_element(By.LINK_TEXT, 'Contact Us').text
        assert contact_text == contact
