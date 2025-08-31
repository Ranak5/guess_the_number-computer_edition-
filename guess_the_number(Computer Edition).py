#Guess the number (Computer edition)
import random
def computer_guess():
    number = 89
    i = 0    
    while 1:
        num = random.randint(1,100)        
        if number == num:
            print(f"Congrats you guessed it : {num}  , It took {i} attempts to guess the right one")
            break
        else:
            print("Try Again")
        i += 1            
computer_guess()
