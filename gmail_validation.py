email = input("Enter you email: ")

if len(email) >= 6:

    if email[0].isalpha():
        

        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):

                print("right")
            else:
                print("wrong place of dot")
        else:
            print("wrong Email: Due to @.")


    else:
        print("Wrong Email: because 1st character is not alphabet")

else:
    print("Wrong Email: because of minimum length")
    