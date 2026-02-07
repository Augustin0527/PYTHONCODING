("===========login system==========")
while True:
    try:
        age= int(input("enter your age minimum 10:"))
    except ValueError as e:
        print ("invalid input try again")
        continue
    if age >=10:
         name = input("enter your name:")
         pasword = input("enter your passsword:")
         print (" signup successful")
         break 
    else:
        print ("sorry we c'ant  proceed")
        continue 
