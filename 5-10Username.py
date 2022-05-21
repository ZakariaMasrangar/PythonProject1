current_users = ['samuel', 'aquilas', 'admin', 'zaki', 'david']
new_users = ['ange', 'zoro', 'marquise', 'denzel', 'wanda']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")