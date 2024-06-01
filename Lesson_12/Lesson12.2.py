class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}"


class Customer:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Phone: {self.phone_number}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity

    def total_price(self):
        total = 0
        for product, quantity in self.products.items():
            total += product.price * quantity
        return total

    def __str__(self):
        products_info = "\n".join([f"{product.name}: {quantity} pcs." for product, quantity in self.products.items()])
        return f"Customer: {self.customer}\nProducts:\n{products_info}\nTotal price: {self.total_price()}"


# Creating instances of Product class
product1 = Product("Laptop", 1200, "High-performance laptop", "15 inch")
product2 = Product("Smartphone", 800, "Latest smartphone model", "6 inch")

# Creating instance of Customer class
customer = Customer("John", "Doe", "123456789")

# Creating instance of Order class
order = Order(customer)
order.add_product(product1, 2)
order.add_product(product2, 1)

# Testing
print(order)
