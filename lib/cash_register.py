#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize the register's attributes.
        self._discount = 0
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Validate the discount percentage."""
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, title, price, quantity=1):
        """Add an item and update the register total."""
        self.total += price * quantity

        # Add the item name once for each unit purchased.
        for _ in range(quantity):
            self.items.append(title)

        # Record the transaction so it can be reversed.
        self.previous_transactions.append({
            "item": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the discount and print the updated total."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total *= (100 - self.discount) / 100

        print(
            f"After the discount, the total comes to ${self.total:g}."
        )

    def void_last_transaction(self):
        """Remove the most recently added transaction."""
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        # Reverse the transaction's effect on the total.
        self.total -= (
            transaction["price"] * transaction["quantity"]
        )

        # Remove the corresponding item names.
        for _ in range(transaction["quantity"]):
            self.items.remove(transaction["item"])
