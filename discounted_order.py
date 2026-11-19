
"""
Program: Discounted Order System
Description: Apply a 10% discount using inheritance.
"""


class Order:
    """Represent an order with its ID and total amount."""

    def __init__(self, order_id, total):
        """Initialize the order details."""
        self.order_id = order_id
        self.total = total

    def calculate_total(self):
        """Return the original order total."""
        return self.total


class DiscountedOrder(Order):
    """Represent an order with a 10% discount."""

    def calculate_total(self):
        """Calculate the total after applying a 10% discount."""
        original_total = super().calculate_total()
        discount = original_total * 0.10
        return original_total - discount


def main():
    """Create an order and display its discounted total."""
    order = DiscountedOrder("ORD001", 1200)

    print(f"Order ID: {order.order_id}")
    print(f"Original Total: {order.total}")
    print(f"Discounted Total: {order.calculate_total()}")


if __name__ == "__main__":
    main()