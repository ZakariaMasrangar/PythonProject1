class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("  first_name: " + self.first_name)
        print("  last_name: " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

zaki = User('zak', 'zaka', 'zakizaka', 'zaki@example.com', 'mesquite')
zaki.describe_user()
zaki.greet_user()

print("\nMaking 3 login attempts...")
zaki.increment_login_attempts()
zaki.increment_login_attempts()
zaki.increment_login_attempts()
print("  Login attempts: " + str(zaki.login_attempts))

print("Resetting login attempts...")
zaki.reset_login_attempts()
print("  Login attempts: " + str(zaki.login_attempts))