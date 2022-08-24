# https://www.youtube.com/watch?v=OKuiyX5k6zg&list=WL&index=8&t=4023s

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2, 3}$"
user_email = input("Enter your email: ")

if (re.search(email_condition, user_email)):
    print("Email verified")
else:
    print("Invalid Email")