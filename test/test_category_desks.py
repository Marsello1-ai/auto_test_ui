def test_count_filters(category_desks):
    category_desks.open_page()
    category_desks.check_filters_quantity_on_page(3)


def test_display_as_a_list(category_desks):
    category_desks.open_page()
    category_desks.display_as_a_list()


def test_product_card(category_desks):
    category_desks.open_page()
    category_desks.check_product_name_in_card_on_page()
