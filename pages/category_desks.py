from pages.base_page import MainPage
from utils.test_data import card_name_desk
from selenium.webdriver.common.by import By


class CategoryDesks(MainPage):
    page_url = '/shop/category/desks-1'

    def count_filters(self):
        count = 3
        check_box = self.driver.find_elements(By.CSS_SELECTOR, 'div.flex-column.mb-3 div.form-check')
        assert len(check_box) == count

    def checking_the_location(self):
        category_list = self.driver.find_element(By.CSS_SELECTOR, '[for="o_wsale_apply_list"]')
        category_list.click()
        list_button = self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-light.o_wsale_apply_list.active')
        assert 'active' in list_button.get_attribute('class')

    def product_card(self):
        desk_with_screen = self.driver.find_element(
            By.CSS_SELECTOR, '[alt="[FURN_7888] Desk Stand with Screen"]'
        )
        desk_with_screen.click()
        title_name = self.driver.find_element(By.TAG_NAME, 'h1').text
        assert card_name_desk == title_name
