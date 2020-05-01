import random
print("Hello! Welcome to the Guessing Game! The rules are: You have unlimited tries and you have to choose a number through 1-10, or else it will say Sorry! Thats the wrong number.")
a = random.randint(1, 10)

while True:
    number = input("Enter a number: ")

    if int(number) == a:
        print("You win!")
        break;
    else:
        print("Sorry, thats the wrong number.")
