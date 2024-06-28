email = input("Enter you email: ")

j,k,d = 0,0,0
if len(email) >= 6:

    if email[0].isalpha():
        

        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):

                for i in email:
                    if i ==  i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1


                    if j == 1 or k == 1 or d == 1:
                        print("wrong email")
                    else:
                        print("your email is right")
            else:
                print("wrong place of dot")
        else:
            print("wrong Email: Due to @.")


    else:
        print("Wrong Email: because 1st character is not alphabet")

else:
    print("Wrong Email: because of minimum length")
    