class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        message = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + message)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        message = self.restaurant_name + " is open."
        print("\n" + message)

restaurant = Restaurant('Barbecue', 'Taco Bell')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
