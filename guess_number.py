number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while True:
    print(f"Sorry! That's incorrect.")

    if int(guess) < number: print("Guess higher...")
    else: print("Guess lower...")

    guess = input("Guess again (enter q to exit): ")

    if guess == "q":
        print(f"The number was {number}") 
        break

    if int(guess) == number:
        print("That is correct!")
        break

