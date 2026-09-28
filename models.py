"""
ByteBites -- core object model.

Four classes, taken from bytebites_design.mmd:

- Customer:  a real person using the app. Holds a name and a purchase
             history of past Orders, which is how the system tells a
             returning customer from a first-time one.
- MenuItem:  one sellable item. Holds name, price, category, popularity.
- Menu:      the full catalog of MenuItems. Can filter by category and
             sort by popularity.
- Order:     one transaction. Holds a Customer and the selected
             MenuItems, and computes the total cost.
"""


class Customer:
    """A ByteBites user, identified by name and their past orders."""

    def __init__(self, name: str):
        self.name = name
        # Spec decision (see bytebites_spec.md): a "purchase" is a
        # completed Order, not a loose MenuItem.
        self.purchase_history: list["Order"] = []

    def record_purchase(self, order: "Order") -> None:
        """Append a completed order to this customer's history."""
        self.purchase_history.append(order)

    def is_returning_customer(self) -> bool:
        """True once the customer has at least one past order."""
        return len(self.purchase_history) > 0


class MenuItem:
    """One sellable food or drink item."""

    def __init__(self, name: str, price: float, category: str, popularity: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity


class Menu:
    """The full collection of MenuItems available to order."""

    def __init__(self):
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add one item to the catalog."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[MenuItem]:
        """Return every item in one category, e.g. "Drinks" or "Desserts"."""
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self) -> list[MenuItem]:
        """Return the items most popular first, leaving self.items untouched."""
        return sorted(self.items, key=lambda item: item.popularity, reverse=True)


class Order:
    """One transaction: a customer plus the items they picked."""

    def __init__(self, customer: Customer):
        self.customer = customer
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add one item to this order."""
        self.items.append(item)

    def calculate_total(self) -> float:
        """Sum the price of every item in the order. An empty order costs 0."""
        return sum(item.price for item in self.items)


def _demo() -> None:
    """Manual scenario: build a few objects and exercise every method."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.50, "Entrees", 4.7))
    menu.add_item(MenuItem("Large Soda", 2.25, "Drinks", 3.9))
    menu.add_item(MenuItem("Iced Coffee", 3.75, "Drinks", 4.9))
    menu.add_item(MenuItem("Brownie", 4.00, "Desserts", 4.2))

    print("-- objects store what the diagram says --")
    first = menu.items[0]
    print(f"MenuItem: {first.name} | ${first.price} | {first.category} | {first.popularity}")
    print(f"Menu holds {len(menu.items)} items")

    print("\n-- filter by category --")
    for item in menu.filter_by_category("Drinks"):
        print(f"  Drinks: {item.name}")

    print("\n-- sort by popularity --")
    for item in menu.sort_by_popularity():
        print(f"  {item.popularity}  {item.name}")

    print("\n-- order total --")
    mathew = Customer("Mathew")
    print(f"Returning customer before ordering? {mathew.is_returning_customer()}")

    empty_order = Order(mathew)
    print(f"Empty order total: ${empty_order.calculate_total():.2f}")

    order = Order(mathew)
    order.add_item(menu.items[0])   # Spicy Burger 8.50
    order.add_item(menu.items[1])   # Large Soda   2.25
    print(f"Order for {order.customer.name}: ${order.calculate_total():.2f}")

    mathew.record_purchase(order)
    print(f"Returning customer after ordering? {mathew.is_returning_customer()}")
    print(f"Purchase history length: {len(mathew.purchase_history)}")


if __name__ == "__main__":
    _demo()
