# ByteBites Design Reference

Shared context for any AI coding assistant working on the ByteBites backend.
Attach this file to a chat instead of repeating the same rules every message.

## Project Snapshot

ByteBites is a campus food ordering backend. This tinker builds the core
object model only: no database, no web framework, no payment processing,
no recommendation engine.

## Behavioral Instructions

1. **Stay inside the four candidate classes.** `Customer`, `MenuItem`,
   `Menu`, `Order`. Do not invent `Payment`, `Restaurant`, `User`,
   `Cart`, `RecommendationEngine`, or any abstract base class. If you
   believe another class is needed, say so in prose and wait — do not
   add it to the diagram or the code.
2. **The spec is the source of truth.** Every attribute must trace back to
   a sentence in `bytebites_spec.md`. If the spec does not mention it
   (IDs, timestamps, addresses, tax, discounts, delivery), leave it out.
3. **No inheritance.** Relationships in this system are "has a"
   (association, `-->` in Mermaid), not "is a" (`--|>`).
4. **Plain Python only.** Standard library, no dataclasses, no Pydantic,
   no external packages. `pytest` is allowed in test files only.
5. **Flag assumptions instead of silently choosing.** When the spec is
   ambiguous (for example, what `purchase_history` holds), state the
   options, recommend one, and mark the choice in a comment.
6. **Small, readable methods.** One job per method, a one-line docstring,
   type hints on parameters and return values. No clever one-liners.
7. **Do not add error handling the spec did not ask for.** No custom
   exception classes, no input validation beyond what a listed behavior
   requires.
8. **Mermaid output must be `classDiagram`** with `+` visibility markers
   and typed attributes, pasteable into the Mermaid Live Editor with no
   edits. Return the raw code block, not a picture or a description.
9. **Show your reasoning before code changes** when a request is
   ambiguous, so the change can be accepted or rejected before it lands.

## Vocabulary

- **Item** = one sellable product (`MenuItem`), never a line in an order.
- **Menu** = the full catalog of items, not a subset.
- **Order** = one transaction for one customer.
- **Popularity** = a 0-5 rating used for sorting, not a sales count.
