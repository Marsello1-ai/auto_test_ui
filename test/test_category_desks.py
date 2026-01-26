def test_count_filters(category_desks):
    category_desks.open_page()
    category_desks.check_filters_quantity_on_page(3)


def test_checking_the_location(category_desks):
    category_desks.open_page()
    category_desks.checking_the_location()


def test_product_card(category_desks):
    category_desks.open_page()
    category_desks.product_card()
