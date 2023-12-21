user_names= ['eric', 'alice', 'bob', 'admin', 'charlie', 'david']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status reort?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")
