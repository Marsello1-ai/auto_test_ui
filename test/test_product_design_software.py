def test_title_page(product_design_software):
    product_design_software.open_page()
    product_design_software.check_page_title()


def test_buy_two_design(product_design_software):
    product_design_software.open_page()
    product_design_software.buy_two_product()


def test_delete_buy(product_design_software):
    product_design_software.open_page()
    product_design_software.buy_two_product()
    product_design_software.delete_buy()
