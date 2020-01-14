current_users = ['admin', 'vc', 'alien', 'alina', 'josh']
new_users = ['Admin', 'VC', 'Crush', 'Ben', 'James']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("This username is existing in our system, please rename again.")
    else:
        print("This username is alivable.")