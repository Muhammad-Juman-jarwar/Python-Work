print("Welcome to my program")
print("1: for tables")
print("2: for my shop")
print("3: for the school system")
print("4: for Calculating the electricity bill")
print("5: for Exiting the program")

selections=int(input("Please select from the given options to reach your destination"))
if selections==1:
    print("Welcome to the tables program")
    firstno=int(input("Please write your first no of table kindly"))
    secondno=int(input("Please write your second no of table kindly"))
    for table in range(firstno,secondno+1):
        for table2 in range(1,10+1):
            print(table,"X",table2,"=",table*table2)

elif selections==2:
    
    from os import stat_result


    employ1=["Ahsan","100 Rs","3000 Rs","ahsan123"]
    employ2 = ["Naveed", "100 Rs", "3000 Rs", "naveed123"]

    product1=["Solar Plates","24000 Rs","24 In Stock","1"]
    product2=["Fans","2000 Rs","20 In Stock","12"]
    product3=["Tube lights","1500 Rs","15 In Stock","123"]
    product4=["Sewing Machines","10000 Rs","10 In Stock","1234"]
    product5=["Washing Machines","30000 Rs","30 In Stock","12345"]

    print("Welcme to my Shop")

    print("1: Employes Management")
    print("2: Product Management")
    print("3: Expense Management")

    list=["1","2","3"]

    sel=input("select from given options to open its panel")

    if sel==list[0]:

        print("Welcome to Employes Management Section")
        print("1: Employes Information")
        print("2: Employes Attendance")

        list1=["1","2"]

        sel1=input("Please select any option from above.")

        if sel1==list[0]:

            print("1: Ahsan")
            print("2: Naveed")

            list2=["1","2"]
        
            sel2=input("select from above given options to open your employes information")

            if sel2==list2[0]:
                print("Name = ",employ1[0])
                print("Daily Salary = ",employ1[1])
                print("Monthly Salary = ",employ1[2])
                print("ID = ",employ1[3])
                td=["1"]
                em=input("Click 1 if you wanna update the employe information")
                if em==td[0]:
                    employ1.clear()
                    x=input("Enter Name")
                    y=input("Enter Daily Salary")
                    z=input("Enter Monthly Salary")
                    employ1.insert(0,x)
                    employ1.insert(1,y)
                    employ1.insert(2,z)
                else:
                    print("You Choose a different option so Good Bye")
            elif sel2==list2[1]:
                print("Name = ", employ2[0])
                print("Daily Salary = ", employ2[1])
                print("Monthly Salary = ", employ2[2])
                print("ID = ", employ2[3])
                em1 = input("Click 1 if you wanna update the employe information")
                td1=["1"]
                if em1 == td1[0]:
                    employ1.clear()
                    x1 = input("Enter Name")
                    y1 = input("Enter Daily Salary")
                    z1 = input("Enter Monthly Salary")
                    employ2.insert(0, x1)
                    employ2.insert(1, y1)
                    employ2.insert(2, z1)
                else:
                    print("You Choose a different option so Good Bye")    
            else:
                print("You Choose a different option so Good Bye")

        elif sel1==list[1]:

            print("1: Ahsan")
            print("2: Naveed")
        
            list3=["1","2"]

            sel3=input("select from above given options to Feed your employ's attendance")
        
            if sel3==list3[0]:
                a=int(input("Please mention How Many Days Ahsan was present in the shop = "))
                print("This Month Ahsan's Salary would be = ",a*100)
            elif sel3==list3[1]:
                b=int(input("Please mention How Many Days Naveed was present in the shop = "))
                print("This Month Naveed's Salary would be = ",b*100)
            else:
                print("You Choose the Wrong Option So Good Bye")
        else:
            print("You Choose the Wrong Option So Good Bye")

    elif sel==list[1]:
        print("Welcome to Product Management Section")
        
        print("1: Products Information")
        print("2: Update Products Information")

        list4=["1","2"]
        sel4=input("Choose any option you want")

        if sel4==list4[0]:
            print("Welcome to Products information section choose any product to see its information")
            productlist=["1","2","3","4","5","6"]
            productsel=input("Select from given options to open its infromation")
            print("1: Solar Plate")
            print("2: Fan")
            print("3: Tube-light")
            print("4: Sewing Machine")
            print("5: Washing Machine")
            print("6: All Products")
            if productsel==productlist[0]:
                print("Name = ", product1[0])
                print("Price = ", product1[1])
                print("Quantity Available = ", product1[2])
                print("ID = ", product1[3])
                pr1=input("Click 1 if you want to update the information")
                if pr1==1:
                    product1.clear()
                    print("Your previous product infromation is deleted successfully    now you can place another one")
                    g1=input("Name = ")
                    g2=input("Price = ")
                    g3=input("Quantity = ")
                    product1.insert(0,g1)
                    product1.insert(1,g2)
                    product1.insert(2,g3)
                    print(product1)
                    print("Congratulations Your product has been updated    successfully")                

            elif productsel == productlist[1]:
                print("Name = ", product2[0])
                print("Price = ", product2[1])
                print("Quantity Available = ", product2[2])
                print("ID = ", product2[3])
                pr2=input("Click 1 if you want to update the information")
                if pr2==1:
                    product2.clear()
                    print(
                    "Your previous product infromation is deleted successfully now you can place another one")
                    h1 = input("Name = ")
                    h2 = input("Price = ")
                    h3 = input("Quantity = ")
                    product2.insert(0, h1)
                    product2.insert(1, h2)
                    product2.insert(2, h3)
                    print(product2)
                    print("Congratulations Your product has been updated successfully")

            elif productsel == productlist[2]:
                print("Name = ", product3[0])
                print("Price = ", product3[1])
                print("Quantity Available = ", product3[2])
                print("ID = ", product3[3])
                pr3=input("Click 1 if you want to update the information")
                if pr3==1:
                    product3.clear()
                    print(
                    "Your previous product infromation is deleted successfully now you can place another one")
                    i1 = input("Name = ")
                    i2 = input("Price = ")
                    i3 = input("Quantity = ")
                    product3.insert(0, i1)
                    product3.insert(1, i2)
                    product3.insert(2, i3)
                    print(product3)
                    print("Congratulations Your product has been updated successfully")
            
            elif productsel == productlist[3]:
                print("Name = ", product4[0])
                print("Price = ", product4[1])
                print("Quantity Available = ", product4[2])
                print("ID = ", product4[3])
                pr4=input("Click 1 if you want to update the information")
                if pr4==1:
                    product4.clear() 
                    print("Your previous product infromation is deleted successfully now you can place another one")            
                    j1=input("Name = ")
                    j2=input("Price = ")
                    j3=input("Quantity = ")
                    product4.insert(0,j1)
                    product4.insert(1,j2)
                    product4.insert(2,j3)
                    print(product4)
                    print("Congratulations Your product has been updated successfully")
            
            elif productsel == productlist[4]:
                print("Name = ", product5[0])
                print("Price = ", product5[1])
                print("Quantity Available = ", product5[2])
                print("ID = ", product5[3])
                pr5 = input("Click 1 if you want to update the information")
                if pr5 == 1:
                    product5.clear()
                    print("Your previous product infromation is deleted successfully now you can place another one")
                    k1=input("Name = ")
                    k2=input("Price = ")
                    k3=input("Quantity = ")
                    product5.insert(0,k1)
                    product5.insert(1,k2)
                    product5.insert(2,k3)
                    print(product5)
                    print("Congratulations Your product has been updated successfully")
            
            elif productsel == productlist[5]:
                print("product no = 1")
                print("Name = ", product1[0])
                print("Price = ", product1[1])
                print("Quantity Available = ", product1[2])
                print("ID = ", product1[3])
                print("product no = 2")
                print("Name = ", product2[0])
                print("Price = ", product2[1])
                print("Quantity Available = ", product2[2])
                print("ID = ", product2[3])
                print("product no = 3")
                print("Name = ", product3[0])
                print("Price = ", product3[1])
                print("Quantity Available = ", product3[2])
                print("ID = ", product3[3])
                print("product no = 4")
                print("Name = ", product4[0])
                print("Price = ", product4[1])
                print("Quantity Available = ", product4[2])
                print("ID = ", product4[3])
                print("product no = 5")
                print("Name = ", product5[0])
                print("Price = ", product5[1])
                print("Quantity Available = ", product5[2])
                print("ID = ", product5[3])

            else:
                print("You Choose the Wrong Option So Good Bye")    

        elif sel4 == list4[1]:
            print("Welcome to Update Products information section choose any product to update its information")
            productlist2 = ["1", "2", "3", "4", "5", "6"]
            productsel2 = input("Select from given options to update its infromation")
            print("1: Solar Plate")
            print("2: Fan")
            print("3: Tube-light")
            print("4: Sewing Machine")
            print("5: Washing Machine")

            if productsel2==productlist2[0]:
                product1.clear()
                print("Your previous product infromation is deleted successfully now you can place another one")
                b1=input("Name = ")
                b2=input("Price = ")
                b3=input("Quantity = ")
                product1.insert(0,b1)
                product1.insert(1,b2)
                product1.insert(2,b3)
                print(product1)
                print("Congratulations Your product has been updated successfully")
            elif productsel2==productlist2[1]:
                product2.clear()
                print("Your previous product infromation is deleted successfully now you can place another one")
                c1 = input("Name = ")
                c2 = input("Price = ")
                c3 = input("Quantity = ")
                product2.insert(0, c1)
                product2.insert(1, c2)
                product2.insert(2, c3)
                print(product2)
                print("Congratulations Your product has been updated successfully")
            elif productsel2==productlist2[2]:
                product3.clear()
                print("Your previous product infromation is deleted successfully now you can place another one")            
                d1=input("Name = ")
                d2=input("Price = ")
                d3=input("Quantity = ")
                product3.insert(0,d1)
                product3.insert(1,d2)
                product3.insert(2,d3)
                print(product3)
                print("Congratulations Your product has been updated successfully")
            elif productsel2==productlist2[3]:
                product4.clear() 
                print("Your previous product infromation is deleted successfully now you can place another one")            
                e1=input("Name = ")
                e2=input("Price = ")
                e3=input("Quantity = ")
                product4.insert(0,e1)
                product4.insert(1,e2)
                product4.insert(2,e3)
                print(product4)
                print("Congratulations Your product has been updated successfully")
            elif productsel2==productlist2[4]:
                product5.clear()
                print("Your previous product infromation is deleted successfully now you can place another one")
                f1=input("Name = ")
                f2=input("Price = ")
                f3=input("Quantity = ")
                product5.insert(0,f1)
                product5.insert(1,f2)
                product5.insert(2,f3)
                print(product5)
                print("Congratulations Your product has been updated successfully")
            else:    
                print("You Choose the Wrong Option So Good Bye")

    elif sel==list[2]:
        print("Welcome to Expence Management Section")
        total=int(input("How Much money you earned this month =Rs "))
        tea=int(input("How much money you spent on tea this month =Rs "))
        customerwelfare=int(input("How much money you spent for customers this month =Rs "))
        others=int(input("How much money you spent this month on other things =Rs "))

        sal=int(total-tea-customerwelfare-others)
        print("you Saved=" ,sal,"Rs this Month after all neccessary Expenses")
        employes=int(input("How Much salary you gave to your Employs this month =Rs "))
        print("Your Personal profit after all the things and employes salary has become = ",sal-employes,"Rs in this month")

elif selections==3:
    print("Welcome to the school system")

    student1=["awais","12345","3rd","awais123"]
    student2=["haris","123456","3rd","haris123"]
    student3=["shakeel","1234567","3rd","shakeel123"]
    student4 =["jawad", "12345678", "3rd", "jawad123"]
    student5 =["mohsin", "123456789", "3rd", "mohsin123"]

    names=["1","2","3","4","5","6"] 

    teacher1=["ahsan","321","biology","ahsan123"]
    teacher2=["jameel","4321","chemistry","jameel123"]

    list=("1","2","3","4")

    print("welcome to my School")

    a=input("Enter UserName")
    b=input("Enter Your Password")
    if a==student1[3] and b==student1[1]:
        print("Name = ",student1[0])
        print("Password = ",student1[1])
        print("Class = ",student1[2])
        print("UserName/ID = ",student1[3])
    elif a==student2[3] and b==student2[1]:
        print("Name =", student2[0])
        print("Password = ",student2[1])
        print("Class = ",student2[2])
        print("UserName/ID = ",student2[3])
    elif a==student3[3] and b==student3[1]:
        print("Name =", student3[0])
        print("Password = ", student3[1])
        print("Class = ", student3[2])
        print("UserName/ID = ", student3[3])

    elif a==student4[3] and b==student4[1]:
        print("Name =", student4[0])
        print("Password = ", student4[1])
        print("Class = ", student4[2])
        print("UserName/ID = ", student4[3])

    elif a==student5[3] and b==student5[1]:
        print("Name =", student5[0])
        print("Password = ", student5[1])
        print("Class = ", student5[2])
        print("UserName/ID = ", student5[3])

    elif a==teacher1[3] and b==teacher1[1]:

        print("WELCOME TO THE TEACHERS DASHBOARD")
        print("1: Check Students Records")
        print("2: Update Students Records")
        print("3: Delete Students Records")
        print("4: Exit the Program")

        options=input("Select From Given options 1 to 4")

        if list[0]==options:
            print("Welcome to the students records")
            print("1: awais")
            print("2: haris")
            print("3: shakeel")
            print("4: jawad")
            print("5: mohsin")
            print("6: all of them")
            studentsnames=input("select any option from above to check record")
            if names[0]==studentsnames:
                print("Name = ",student1[0])
                print("Password = ",student1[1])
                print("Class = ",student1[2])
                print("UserName/ID = ",student1[3])    
            elif names[1]==studentsnames:
                print("Name =", student2[0])
                print("Password = ", student2[1])
                print("Class = ", student2[2])
                print("UserName/ID = ", student2[3])
            elif names[2]==studentsnames:
                print("Name =", student3[0])
                print("Password = ", student3[1])
                print("Class = ", student3[2])
                print("UserName/ID = ", student3[3])
            elif names[3]==studentsnames:
                print("Name =", student4[0])
                print("Password = ", student4[1])
                print("Class = ", student4[2])
                print("UserName/ID = ", student4[3])
            elif names[4]==studentsnames:
                print("Name =", student5[0])
                print("Password = ", student5[1])
                print("Class = ", student5[2])
                print("UserName/ID = ", student5[3])
            elif names[5]==studentsnames:
                print("student no 1")
                print("Name = ", student1[0])
                print("Password = ",student1[1])
                print("Class = ",student1[2])
                print("UserName/ID = ",student1[3]) 

                print("student no 2")
                print("Name =", student2[0])
                print("Password = ", student2[1])
                print("Class = ", student2[2])
                print("UserName/ID = ", student2[3])

                print("student no 3")
                print("Name =", student3[0])
                print("Password = ", student3[1])
                print("Class = ", student3[2])
                print("UserName/ID = ", student3[3])

                print("student no 4")
                print("Name =", student4[0])
                print("Password = ", student4[1])
                print("Class = ", student4[2])
                print("UserName/ID = ", student4[3])

                print("student no 5")
                print("Name =", student5[0])
                print("Password = ", student5[1])
                print("Class = ", student5[2])
                print("UserName/ID = ", student5[3])

        elif list[1]==options:

            
            print("Welcome to the students records")
            print("1: awais")
            print("2: haris")
            print("3: shakeel")
            print("4: jawad")
            print("5: mohsin")
            print("6: all of them")
            studentsnames = input("Select any student to update its record")
            if names[0]==studentsnames:
                student1.clear()
                a=input("Name = ")
                b=input("Password = ")
                c=input("Class = ")
                d=input("UserName/ID = ")
                student1.insert(0,a)
                student1.insert(1,b)
                student1.insert(2,c)
                student1.insert(3,d)
                print("Congratulations Student Account is Updated Successfully")
            elif names[1] == studentsnames:
                student2.clear()
                a = input("Name = ")
                b = input("Password = ")
                c = input("Class = ")
                d = input("UserName/ID = ")
                student2.insert(0, a)
                student2.insert(1, b)
                student2.insert(2, c)
                student2.insert(3, d)
                print("Congratulations Student Account is Updated Successfully")
            elif names[2] == studentsnames:
                student3.clear()
                a = input("Name = ")
                b = input("Password = ")
                c = input("Class = ")
                d = input("UserName/ID = ")
                student3.insert(0, a)
                student3.insert(1, b)
                student3.insert(2, c)
                student3.insert(3, d)
                print("Congratulations Student Account is Updated Successfully")
            elif names[3] == studentsnames:
                student4.clear()
                a = input("Name = ")
                b = input("Password = ")
                c = input("Class = ")
                d = input("UserName/ID = ")
                student4.insert(0, a)
                student4.insert(1, b)
                student4.insert(2, c)
                student4.insert(3, d)
                print("Congratulations Student Account is Updated Successfully")
            elif names[4] == studentsnames:
                student5.clear()
                a = input("Name = ")
                b = input("Password = ")
                c = input("Class = ")
                d = input("UserName/ID = ")
                student5.insert(0, a)
                student5.insert(1, b)
                student5.insert(2, c)
                student5.insert(3, d)
                print("Congratulations Student Account is Updated Successfully")

        elif list[2] == options:
            print("Welcome to the students records")
            print("1: awais")
            print("2: haris")
            print("3: shakeel")
            print("4: jawad")
            print("5: mohsin")
            print("6: all of them")
            studentsnames = input("Select any student  to Delete its record")
            if names[0] == studentsnames:
                true=["yes","no"]
                bolean=input("Do you really want to delete write yes other wise write no ")
                if true[0]==bolean:
                    student1.clear()
                    print("Congratulations Student Account is Deleted Successfully")
                else:
                    print(student1)

            elif names[1] == studentsnames:
                true = ["yes", "no"]
                bolean = input(
                    "Do you really want to delete write yes other wise write no ")
                if true[0] == bolean:
                    student2.clear()
                    print("Congratulations Student Account is Deleted Successfully")
                else:
                    print(student2)
                
            elif names[2] == studentsnames:
                true = ["yes", "no"]
                bolean = input(
                    "Do you really want to delete write yes other wise write no ")
                if true[0] == bolean:
                    student3.clear()
                    print("Congratulations Student Account is Deleted Successfully")
                else:
                    print(student3)
            elif names[3] == studentsnames:
                true = ["yes", "no"]
                bolean = input(
                    "Do you really want to delete write yes other wise write no ")
                if true[0] == bolean:
                    student4.clear()
                    print("Congratulations Student Account is Deleted Successfully")
                else:
                    print(student4)
            elif names[4] == studentsnames:
                true = ["yes", "no"]
                bolean = input(
                    "Do you really want to delete write yes other wise write no ")
                if true[0] == bolean:
                    student5.clear()
                    print("Congratulations Student Account is Deleted Successfully")
                else:
                    print(student5)
            elif names[5] == studentsnames:
                true = ["yes", "no"]
                bolean = input(
                    "Do you really want to delete write yes other wise write no ")
                if true[0]==bolean:    
                    student1.clear()
                    student2.clear()
                    student3.clear()
                    student4.clear()
                    student5.clear()
                    print("Congratulations All Students Accounts Are Deleted Successfully")
                else:
                    print(student1)
                    print(student2)
                    print(student3)
                    print(student4)
                    print(student5)

        if list[3]==options:
            exit()

    else:
        print("Your Username or Password is Wrong So")
        print("Good Bye")
        
elif selections==4:
    print("Welcome to the Electricity Bill Calculating system")
    a=int(input("Please Enter your Electricity Usage Days = "))
    if a <=100:
        b=a*15
    elif a<=200:
        b=1500+(a-100)*20
    elif a<=300:
        b=1500+2000+(a-200)*25
    elif a<=400:
        b=1500+2000+2500+(a-300)*30
    elif a<=500:
        b=1500+2000+2500+3000+(a-400)*35
    elif a<=600:
        b=1500+2000+2500+3000+3500+(a-500)*40
    elif a<=700:
        b=1500+2000+2500+3000+3500+4000+(a-600)*45
    elif a<=800:
        b=1500+2000+2500+3000+3500+4000+4500+(a-700)*50
    elif a<=900:
        b=1500+2000+2500+3000+3500+4000+4500+5000+(a-800)*55
    elif a<=1000:
        b=1500+2000+2500+3000+3500+4000+4500+5000+5500+(a-900)*60
    elif a<=1100:
        b=1500+2000+2500+3000+3500+4000+4500+5000+5500+6000+(a-1000)*65
    elif a<=1200:
        b=1500+2000+2500+3000+3500+4000+4500+5000+5500+6000+6500+(a-1100)*70
    elif a<=1300:
        b=1500+2000+2500+3000+3500+4000+4500+5000+5500+6000+6500+7000+(a-1200)*75
    elif a<=1400:
        b=1500+2000+2500+3000+3500+4000+4500+5000+5500+6000+6500+7000+7500+(a-1300)*80
    elif a<=1500:
        b=1500+2000+2500+3000+3500+4000+4500+5000+5500+6000+6500+7000+7500+8000+(a-1400)*85
    print(b,"This is your Electricity bill")

elif selections==5:
    print("Exit")
else:
    print("you chose a different option so good bye")

