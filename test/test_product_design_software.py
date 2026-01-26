def test_title_page(product_design_software):
    product_design_software.open_page()
    product_design_software.check_page_title()


def test_buy_two_design(product_design_software):
    product_design_software.open_page()
    product_design_software.buy_two_products_and_check_they_are_in_cart()


def test_delete_buy(product_design_software):
    product_design_software.open_page()
    product_design_software.buy_two_products_and_check_they_are_in_cart()
    product_design_software.check_card_is_empty_after_deleting_products()
