class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print(" first_name: " + self.first_name)
        print(" last_name: " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

zaki = User('Acura', 'Benz', 'Chevy', 'zaki@gmail.com', 'Texas')
zaki.describe_user()
zaki.greet_user()

samuel = User('Toyota', 'Tundra', 'Camaro', 'samuel@gmail.com', 'Cameroon')
samuel.describe_user()
samuel.greet_user() 