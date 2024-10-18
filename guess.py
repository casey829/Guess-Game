import random;

top_range = input("Type a number: ")


if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print('Please type a number larger than 0.')
        quit()
else:
    print('Please type a number.')
    quit()
    
random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    guess_user = input("Make a guess: ")
    
    if guess_user.isdigit():
        guess_user = int(guess_user)
    else:
        print('Please type a number next time')
        continue
    
    if guess_user == random_number:
        print("You got it!")
        break
    else:
        if guess_user > random_number:
            print("You were above the number!")
        else:
            print("You are below the  number")
        
print("You got it in " + str(guesses) + " guesses" )