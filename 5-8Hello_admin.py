usernames = ['samuel', 'zaki', 'admin', 'david', 'aquilas']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")