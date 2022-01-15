from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

""" Function to check user's guess against actual answer """
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low") 
        return turns -1
    else:
        print("You got it!!")
def set_difficulty():
    level = input("Choose a difficulty.Type 'Easy' or 'Hard': ")
    if level == "Easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the number guessing name !!")
    print("I'm thinking a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Hey you there!! The correct answer is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0 :
            print("You have runned out of guesses")
            return
        elif guess != answer:
            print("Guess again")
game()