import random
attempt_list = []

def show_score():
    if len(attempt_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempt_list)))

def game():
    random_num = int(random.randint(1, 10))
    print("Hey! Welcome to the game of Guesses!")
    player_name = input("What is Your name?")
    play = input("Hi, {}, would you like to play the guessing game? (ENter Yes/No) ".format(player_name))
     
    
    attempt = 0
    show_score()
    while play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 to 15 ")
            if int(guess) < 1 or int(guess) > 15:
                raise ValueError("Please guess a number within the given range ")
            if int(guess) == random_num:
                print("Nice! You got it!")
                attempt += 1
                attempt_list.append(attempt)
                print("It look you {} attempts".format(attempt))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempt = 0
                show_score()
                random_num = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_num:
                print("It's lower")
                attempt += 1
            elif int(guess) < random_num:
                print("It's higher")
                attempt += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    game()