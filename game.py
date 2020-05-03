from random import randint
    
print("============================================")

print("""        
        
        Welcome to single number Roulette

        You will be asked to pick a number from 0 to 36
        
        
        The program will tell you if you guessed the correct number
        
=============================================

        """ )

cont = input("Press enter to continue....")

def Roulette():
    user_num = int(input("Enter a number from 0 to 36: "))

    lucky_num = randint(0, 36)

    if user_num == lucky_num:
        print("Congratulations, You guessed the correct numer! ")
    else:
        print ("Sorry, its not your lucky day. The lucky number was " + str(lucky_num))



Roulette()
print("============================================")



again = input("Wanna try again? yes or no: ")

for i in again:
    if again == "yes":
        Roulette()
    elif again == "no":
        print("Thank you for playing...")
    else:
        print("write 'yes' or 'no' no CAPS")    

