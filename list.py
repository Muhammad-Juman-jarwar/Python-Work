list=["usama","123"]
list1=["1","2","3","4"]     
print("welcome to my facebook")
print("select form given options below")
print("1:login here")
print("2:make an account ")
print("3:update my account ")
print("4:delete account")
ch=input("select form given options 1 to 4")

if list1[0]==ch:  
    print("welcome to the login form")
    a=input("enter your username")
    b=input("enter your password")
    if a==list[0] and b==list[1]:
        print("you succesfully logged in here")
    else:
        print("enter correct password or user name")

elif list1[1]==ch:
    list.clear()
    a=input("enter username")
    b=input("enter your password")
    list.insert(0,a)
    list.insert(1,b)
    print("Congratulations Your account is successfully created")
    print(list[0],list[1])
    
elif list1[2]==ch:
    print("Firstly Enter in your account")
    a=input("enter username")
    b=input("enter your password")
    list.clear()
    a=input("Enter New Username")
    b=input("Enter New Password")
    list.insert(0,a)
    list.insert(1,b)
    print("Congratulations your account is updated succesfully")
    print("welcome to the login form")
    a=input("enter your username")
    b=input("enter your password")
    if a==list[0] and b==list[1]:
        print("you succesfully logged in here")
    else:
        print("enter correct password or user name")

elif list1[3]==ch:
    print("Firstly Enter in your account")
    a=input("enter username")
    b=input("enter your password")
    list.clear()
    print("your account is deleted successfully")
    qr=input("if you wanna make a new account click 2")
    if list1[1]==qr:
        print("create new account")
        a=input("Enter New Username")
        b=input("Enter New Password")
        list.insert(0,a)
        list.insert(1,b)
        print("your new account is succesfully created")
        print("welcome to the login form")
        a=input("enter your username")
        b=input("enter your password")

        if a==list[0] and b==list[1]:
            print("you succesfully logged in here")
        else:
            print("enter correct password or user name")