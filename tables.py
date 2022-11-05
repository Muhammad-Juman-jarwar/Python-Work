j=int(input("enter the choice 1 for program 2 for exit"))     
while j==1:
     a=int(input("Please enter the days of use of electricity"))
     if a<=100:
          print(a*15)
     elif a<=200:
          print(1500+(a-100)*20)
     elif a<=300:
          print(1500+2000+(a-100-100)*25)
     elif a<=300:
          print(1500+2000+2500+(a-100-100-100)*30)
     elif a<=400:
          print(1500+2000+2500+3000+ (a-100-100-100-100)*35)
     
else:
     print("exit")
