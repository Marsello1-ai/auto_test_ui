def test_cart_is_empty(cart_page):
    cart_page.open_page()
    cart_page.empty_cart()


def test_check_number(cart_page):
    cart_page.open_page()
    cart_page.check_number()


def test_contact(cart_page):
    cart_page.open_page()
    cart_page.check_contact()
