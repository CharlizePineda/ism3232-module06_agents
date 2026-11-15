# stock_tool.py
# Author: Charlize Pineda


class StockLookup:
    """A tool that knows how many products are in stock."""

    def __init__(self, stock):
        """Store the stock count this tool can look up."""
        self.stock = stock

    def find_product(self, text):
        """Return the first known product named in the text, or None."""
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return quantity of product in stock, or None if unknown."""
        if product in self.stock:
            return self.stock[product]
        return None

    def check_stock(self, item):
        """Check how many of one product are in stock.

        Args:
            item: The product name, like rain jacket.
        """
        product = self.find_product(item)
        if product is None:
            return "That product was not found."
        return f"We have {self.count_for(product)} of the {product} in stock."
