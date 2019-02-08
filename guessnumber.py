import random
name=input("hello ur name?")
number=random.randint(1,100)
print(name,"think no. betn 1 to 100")
guesstaken=0

while guesstaken<7:
    guess=input("enter a guess")
    guess=int(guess)
    guesstaken=guesstaken+1
    if guess<number:
        print("that was too low")
    elif guess>number:
        print("that was too high")
    else:
        break

if guess==number:
    print("you won ",name)
else:
    print("you lost")
    print("the right no. was ",number)