import random 
def guess():
    print("welcome to guess the number")
    print("the number is between 1 and 10")
    print()

    target= random.randint(1,10)
    attempts = 0  
    while True: 
        try:
            guess = int(input("enter your guess (1-10):")) 
            if guess < 1 or guess > 10 :
                print("enter a number between 1 and 10")
                continue 
        except ValueError : 
            print ("invalid input please enter a number")
            continue
        attempts += 1
        if guess < target :
            print(" too low try again ")
        elif guess > target : 
            print("too high try again")
        else:
            print("correct guess !")
            break
guess()        

    