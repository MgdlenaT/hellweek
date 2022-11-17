from random import randint

while True:
    number = randint(1, 256)
    user_number = False
    while user_number != number:
        try:
            user_number = int(input("Guess the number between 1 to 256: "))
            if user_number > number:
                print("Too much, try again")
            elif user_number < number:
                print("Too small, try again")
                continue
            else:
                print(f"Congratulations, you guessed it! The number is {number}! ")
                user_number = True
                break

        except ValueError:
            print('Try again, use only an integer number')

    users_decision = input("Do you want to play again? Write 'OK'. If not- press anything: ")
    if users_decision.upper() == "OK":
        continue
    else:
        print("Thanks for the game")
        break