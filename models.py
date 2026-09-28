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


class Order:
    """One transaction: a customer plus the items they picked."""

    def __init__(self, customer: Customer):
        self.customer = customer
        self.items: list[MenuItem] = []
