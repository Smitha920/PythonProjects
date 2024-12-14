import random
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choosen_num = random.choice(lst)
print(choosen_num)
flag = False
count = 3
while flag == False:
    num = int(input("guess: "))
    if num == choosen_num:
        print("you win")
        break
    else:
        count-= 1
        print("guess again")
        if count == 0 or num == choosen_num:
            flag = True
            print("out of guess")

