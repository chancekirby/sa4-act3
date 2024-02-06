number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
guess_count = 1
guess_limit = 5

while True:
    print(f"Sorry! That's incorrect.")

    if guess_count >= guess_limit:
        print("Sorry. Out of guesses.")
        print(f"The number was {number}")
        break

    print(f'You have {guess_limit - guess_count} guesses left.')
    guess = input("Guess again (enter q to exit): ")
    guess_count += 1

    if guess == "q":
        print(f"The number was {number}") 
        break

    if int(guess) == number:
        print("That is correct!")
        break
    
    


