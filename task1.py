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
    