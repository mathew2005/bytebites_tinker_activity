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
