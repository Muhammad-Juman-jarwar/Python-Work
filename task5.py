user1=["Ahsan","12345","ahsan123"]
user2=["Juman","12345","juman123"]
print("Welcome to my program")
class my_class:
    def login(self):
        print("Welcome to the login form")
        username=input("Please Enter Your username = ")
        password=input("Please Enter Your Password = ")
        if username==user1[2] and password==user1[1]:
            print("work successful")
            print("Please write 1 if you are super user \n 2 if you are admin")
            usr=input("")
            if usr=='1':
                print("Please choose from the following options \n 1 for purchasing the products \n 2 for selling the products")
                a=int(input(""))
                if a == 1:
                    jeff.purchase()
                elif a==2:
                    #enter the selling function
            elif usr=='2':
                print("you are Admin")
        elif username==user2[2] and password==user2[1]:
            print("again Work successful")
            print("Please write 1 if you are super user \n 2 if you are admin")
            usr=input("")
            if usr=='1':
                print("Please choose from the following options \n 1 for purchasing the products \n 2 for selling the products")
                a=int(input(""))
                if a == 1:
                    jeff.purchase()
                elif a==2:
                    #enter the selling function
            elif usr=='2':
                print("you are Admin")
        else:
            print("Please Enter Correct Credentials")
            jeff.login()
    def purchase(self):
        a ={"name":[], "quantity":[], "price":[]}
        b = list(a.values())
        na = b[0]
        qu = b[1]
        pr = b[2]
        ch = int(input("1 for ADDing the product\n2 to EXIT the program\nEnter your choice : "))
        print("Choose only digits from the given option")
        if ch==1:
            pn = input("Enter product name : ")
            q = input("Enter quantity : ")
            p = float(input("Enter price of the product : "))
            if pn in na:
                ind = na.index(pn)
                qu.insert(ind, q)
                pr.insert(ind, p)
            else:
                na.append(pn)
                qu.append(q)
                pr.append(p)
        elif ch==2:
                print("You have successfully exited the program")
jeff=my_class()
jeff.login()
