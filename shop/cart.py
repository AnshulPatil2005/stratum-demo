"""A cart of items, priced in whole cents."""

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price_cents: int
    quantity: int = 1


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, name: str, price_cents: int, quantity: int = 1) -> None:
        if price_cents < 0 or quantity < 1:
            raise ValueError("a price can't be negative, and a quantity must be at least 1")
        self.items.append(Item(name, price_cents, quantity))

    def total_cents(self) -> int:
        return sum(item.price_cents * item.quantity for item in self.items)
