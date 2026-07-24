import random

# memory + history
memory = {
    "last_difficulty": None,
    "last_secret": None,
    "last_result": None,
    "last_guesses": None
}

def v(key, value):
    # compare
    return key == value

history = []  # game log

def ask_user():
    while True:
        ask = input("Do you want to play guess the number? (type yes or no):").strip().lower()
        if ask not in ["yes","no"]:
            print("Invaild choice, please try again.")
            continue
        if ask == "yes":
            print("Okay lets continue.")
        if ask == "no":
            print("Goodbye.")
        return ask

def ask_difficulty():
    while True:
        ask = input("Which difficulty you want to be set to? (type hard/easy):").strip().lower()
        if ask not in ["hard","easy"]:
            print("Invaild choice, please try again.")
            continue
        break

    if ask == "hard":
        print("Let's continue to hard difficulty.")
    else:
        print("Let's continue to easy difficulty.")
    return ask

def difficulty_easy():
    secret = random.randint(1, 50)
    lives = 10
    guesses_used = 0

    while True:
        guess = input("Guess a number from 1 - 50:").strip()
        if not guess.isdigit():
            print("Invaild choice, please try again.")
            continue
        guess = int(guess)
        break

    while True:
        guesses_used += 1

        if guess == secret:
            print("You got it correct.")
            print("Lives left:", lives)
            update_memory("easy", secret, "win", guesses_used)
            add_history("easy", "win", secret, guesses_used)
            break

        elif guess < secret:
            print("Too low.")
            lives -= 1

        elif guess > secret:
            print("Too high.")
            lives -= 1

        print("Lives left:", lives)

        if lives <= 0:
            print("You ran out of lives.")
            update_memory("easy", secret, "lose", guesses_used)
            add_history("easy", "lose", secret, guesses_used)
            break

        guess = input("Guess again: ").strip()
        if not guess.isdigit():
            print("Invaild choice, please try again.")
            continue
        guess = int(guess)

def difficulty_hard():
    secret = random.randint(1, 100)
    lives = 5
    guesses_used = 0

    while True:
        guess = input("Guess a number from 1 - 100:").strip()
        if not guess.isdigit():
            print("Invaild choice, please try again.")
            continue
        guess = int(guess)
        break

    while True:
        guesses_used += 1

        if guess == secret:
            print("You got it correct.")
            print("Lives left:", lives)
            update_memory("hard", secret, "win", guesses_used)
            add_history("hard", "win", secret, guesses_used)
            break

        elif guess < secret:
            print("Too low.")
            lives -= 1

        elif guess > secret:
            print("Too high.")
            lives -= 1

        print("Lives left:", lives)

        if lives <= 0:
            print("You ran out of lives.")
            update_memory("hard", secret, "lose", guesses_used)
            add_history("hard", "lose", secret, guesses_used)
            break

        guess = input("Guess again: ").strip()
        if not guess.isdigit():
            print("Invaild choice, please try again.")
            continue
        guess = int(guess)

def update_memory(diff, secret, result, guesses):
    # save last game
    memory["last_difficulty"] = diff
    memory["last_secret"] = secret
    memory["last_result"] = result
    memory["last_guesses"] = guesses

def add_history(diff, result, secret, guesses):
    # add game entry
