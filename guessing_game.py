import random

secret_number=random.randint(1,50)
attempts=0
while True:
    guess=input ("Guess a number between 1 and 50:")
    guess=int(guess)
    attempts += 1

    if guess==secret_number:
        print(f"🎉 You got it in {attempts} attempts!")
        break 
    elif guess <secret_number:
        print("Too low!😔 Try higher.")
    else:
        print("Too high!😬 Try lower.")