import random
comp_count = 0
user_count = 0
for i in range(5):
    list = [0, 1, 2]
    comp_guess = random.choice(list)
    #print(comp_guess)
    print("0 : ROCK\n1 : PAPER\n2 : SCISOR")
    user_guess = int(input("guess: "))
    if user_guess < 3:
        if comp_guess == user_guess:
            print("DRAW")
        elif comp_guess == 0 and user_guess == 2:
            print("COMPUTER WIN")
            comp_count +=1
        elif comp_guess == 2 and user_guess == 1:
            print("YOU WIN")
            user_count  +=1
        elif comp_guess > user_guess:
            print("COMPUTER WIN")
            comp_count += 1
        elif user_guess > comp_guess:
            print("YOU WIN")
            user_count += 1
    else:
        print("enter only 0,1,2")
if user_count > comp_count:
    print("winner")
else:
    print("looser")