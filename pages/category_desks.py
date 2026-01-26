from pages.base_page import MainPage
from utils.test_data import card_name_desk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CategoryDesks(MainPage):
    page_url = '/shop/category/desks-1'

    def check_filters_quantity_on_page(self, number_of_filters: int):
        check_box = self.driver.find_elements(By.CSS_SELECTOR, 'div.flex-column.mb-3 div.form-check')
        assert len(check_box) == number_of_filters

    def display_as_a_list(self):
        category_list = self.driver.find_element(By.CSS_SELECTOR, '[for="o_wsale_apply_list"]')
        category_list.click()
        wait = WebDriverWait(self.driver, 10)
        list_button = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.btn.btn-light.o_wsale_apply_list.active')
            )
        )

        assert 'active' in list_button.get_attribute('class')

    def check_product_name_in_card_on_page(self):
        desk_with_screen = self.driver.find_element(
            By.CSS_SELECTOR, '[alt="[FURN_7888] Desk Stand with Screen"]'
        )
        desk_with_screen.click()
        title_name = self.driver.find_element(By.TAG_NAME, 'h1').text
        assert card_name_desk == title_name
