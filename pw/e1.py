from random import randint
# Number guessing game
def guesser(max):
    max = int(max)
    real = randint(0, max)
    while True:
        guess = int(input("What is your guess? "))
        if guess > real:
            print("Too high")
        elif guess < real:
            print("Too low")
        else:
            print("You got it!")
            break

print(guesser(int(input("How high? "))))


