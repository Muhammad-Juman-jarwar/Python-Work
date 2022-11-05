n=int(input("Please enter any no of your choice"))
if n%2==1:
    print(n," Weird")
elif n%2==0 and n>=2 and n<=5:
    print(n," Not Weird")
elif n%2==0 and n>=6 and n<=20: 
    print(n," Weird")
elif n%2==0 and n>20:
    print(n," Not Weird")
