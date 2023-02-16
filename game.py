from random import randint

class Roulette:
    def __init__(self):
        self.user_credit = 0
        self.max_tries = 10
        self.current_try = 0

    def start(self):
        print("============================================")
        print("""        
        Welcome to single number Roulette

        Each try costs 1 credit from the BUY-IN credit balance
        
        If you hit the correct number you will be credited +    36 credits
        =============================================""")
        
        self.user_credit = self.buy_credits()

        while self.current_try < self.max_tries and self.user_credit > 0:
            self.play_round()
            self.current_try += 1
        
        print("============================================")
        print("Game Over! Thank you for playing!")
        print("Total Credit Available Now is:", self.user_credit)
        print("============================================")

    def buy_credits(self):
        while True:
            try:
                user_credit = int(input("Buy In Credit (min 10 credits): "))
                if user_credit < 10:
                    print("Minimum Buy In Credit is 10")
                else:
                    break
            except ValueError:
                print("Invalid input, please enter a valid number")
        print("============================================")
        return user_credit

    def play_round(self):
        print("Remaining Tries:", self.max_tries - self.current_try)
        print("Player Remaining Credit:", self.user_credit)
        while True:
            try:
                user_num = int(input("Enter a number from 0 to 36: "))
                if user_num < 0 or user_num > 36:
                    raise ValueError("Invalid input, please enter a number between 0 and 36")
                break
            except ValueError as e:
                print(e)
        
        lucky_num = randint(0, 36)
        print("The lucky number is:", lucky_num)

        if user_num == lucky_num:
            self.user_credit += 36
            print("""Congratulations, You guessed the correct number!
            You have been credited 36 credits
            Total Credit Available Now is: """ +str(self.user_credit))
        else:
            self.user_credit -= 1
            print("Sorry, it's not your lucky day. You lost 1 credit.")
        
        print("============================================")

roulette = Roulette()
roulette.start()
