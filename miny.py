import random

def guess_the_number():
  number = random.randint(1, 100)
  print("I'm thinking of a number between 1 and 100.")

  while True:
    guess = int(input("What's your guess? "))
    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    else:
      print("You got it! The number was", number)
      break

if __name__ == '__main__':
  guess_the_number()
