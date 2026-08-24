import random

jack = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

count = 1

while guess != jack:

    if guess < jack:
        print(f"Choose a greater number. Attempt: {count}")

    else:
        print(f"Choose a lower number. Attempt: {count}")

    guess = int(input("Enter your guess: "))
    count += 1

print("🎉 Congratulations! You won!")
print("Attempts:", count)
print("Computer's number:", jack)
