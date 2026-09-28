# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions

1. Stay inside the four classes in `bytebites_spec.md`: `Customer`, `MenuItem`,
   `Menu`, `Order`. Do not add `Payment`, `User`, `Cart`, `Restaurant`, or a
   recommendation engine. If you think another class is needed, say so in prose
   and wait — do not put it in the diagram or the code.
2. Every attribute must trace back to a sentence in the spec. No IDs, timestamps,
   tax, tips, discounts, or availability flags.
3. Use "has a" relationships (`-->` in Mermaid), not inheritance (`--|>`).
4. Plain Python and the standard library only. No dataclasses, no external
   packages. `pytest` is allowed in test files.
5. When the spec is ambiguous, state the options and recommend one instead of
   silently choosing, and leave the choice in a comment.
6. Keep methods small: one job each, a one-line docstring, type hints on
   parameters and return values.
7. Do not add validation or custom exceptions the spec did not ask for.
8. Mermaid output must be a `classDiagram` code block with `+` visibility and
   typed attributes, pasteable into the Mermaid Live Editor with no edits.
