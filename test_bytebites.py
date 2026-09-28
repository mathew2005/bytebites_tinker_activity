"""Tests for the ByteBites core object model."""

from models import Customer, Menu, MenuItem, Order


def build_menu() -> Menu:
    """A small catalog used by several tests."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.50, "Entrees", 4.7))
    menu.add_item(MenuItem("Large Soda", 2.25, "Drinks", 3.9))
    menu.add_item(MenuItem("Iced Coffee", 3.75, "Drinks", 4.9))
    menu.add_item(MenuItem("Brownie", 4.00, "Desserts", 4.2))
    return menu


def test_calculate_total_with_multiple_items():
    """An order's total is the sum of its item prices."""
    order = Order(Customer("Mathew"))
    order.add_item(MenuItem("Spicy Burger", 10.00, "Entrees", 4.7))
    order.add_item(MenuItem("Large Soda", 5.00, "Drinks", 3.9))
    assert order.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    """An order with nothing in it costs 0, it does not crash."""
    order = Order(Customer("Mathew"))
    assert order.calculate_total() == 0


def test_filter_by_category_returns_only_that_category():
    """Filtering "Drinks" returns the drinks and nothing else."""
    menu = build_menu()
    drinks = menu.filter_by_category("Drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Coffee"]


def test_filter_by_unknown_category_returns_empty_list():
    """A category no item uses returns an empty list, not an error."""
    menu = build_menu()
    assert menu.filter_by_category("Soup") == []


def test_sort_by_popularity_orders_highest_first():
    """Sorting returns the most popular item first."""
    menu = build_menu()
    ranked = menu.sort_by_popularity()
    assert [item.name for item in ranked] == [
        "Iced Coffee",
        "Spicy Burger",
        "Brownie",
        "Large Soda",
    ]


def test_sort_by_popularity_does_not_reorder_the_menu():
    """Sorting hands back a new list and leaves the catalog untouched."""
    menu = build_menu()
    original = [item.name for item in menu.items]
    menu.sort_by_popularity()
    assert [item.name for item in menu.items] == original


def test_new_customer_is_not_a_returning_customer():
    """A customer with no purchase history is a first-time user."""
    assert Customer("Mathew").is_returning_customer() is False


def test_recording_a_purchase_makes_a_customer_returning():
    """Once an order is recorded, the customer counts as returning."""
    mathew = Customer("Mathew")
    order = Order(mathew)
    order.add_item(MenuItem("Brownie", 4.00, "Desserts", 4.2))
    mathew.record_purchase(order)
    assert mathew.is_returning_customer() is True
    assert mathew.purchase_history == [order]
