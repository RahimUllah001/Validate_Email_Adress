email = input("Enter you email: ")

if len(email) >= 6:

    if email[0].isalpha():
        

        if ("@" in email) and (email.count("@") == 1):
            print("right")


    else:
        print("wrong email")

else:
    print("wrong email")
    