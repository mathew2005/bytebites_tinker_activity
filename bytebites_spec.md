# ByteBites Specification

## Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to
manage our customers, tracking their names and their past purchase history so
the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or
"Large Soda"), so we must track the name, price, category, and popularity
rating for every item we sell.

We also need a way to manage the full collection of items — a digital list
that holds all items and lets us filter by category such as "Drinks" or
"Desserts".

Finally, when a user picks items, we need to group them into a single
transaction. This transaction object should store the selected items and
compute the total cost.

## Candidate Classes

Four nouns the system must model:

1. **Customer** — a real person using the app; holds a `name` and a
   `purchase_history` the system can check to verify they are a returning user.
2. **MenuItem** — one sellable food or drink item; holds `name`, `price`,
   `category`, and `popularity`.
3. **Menu** — the full collection of items; holds every `MenuItem` and can
   filter that collection down to one category.
4. **Order** — one transaction; holds the customer and the selected items, and
   computes the total cost.

## Open Questions / Assumptions

- **What does `purchase_history` hold?** The request says "past purchase
  history" without saying what a purchase is. Options: a list of `MenuItem`
  (every item ever bought) or a list of `Order` (every completed transaction).
  **Decision: a list of `Order`** — a purchase is a transaction, and an order
  already knows its items, so nothing is lost.
- **"Verify they are real users"** is read as the narrow thing the data
  supports: a customer with at least one past order is a returning customer.
  No accounts, passwords, or identity checks are in scope.
- **Popularity** is treated as a 0-5 rating (the request says "popularity
  rating"), not a running count of sales.
