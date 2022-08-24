k, j, d = 0, 0, 0
email = input("Enter your email: ")

if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-4] == '.') ^ (email[-3] == '.'):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i =="__" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                        
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email - No space allowed or No Uppercase ")
                else:
                    print("Email verified")
                
            else:
                print("Invalid email - More than one '.' or wrong positioning of '.'")
        else:
            print("Invalid email - Invalid use of '@'")
    else:
        print("Invalid Email - Email must start with an alphabet")
else:
    print("Invalid Email - Length must be greater than 6")