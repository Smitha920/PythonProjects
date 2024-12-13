print("Welcome to my quiz game")
print("*************************************")
score = 0
q_1 = print("The ability of one class to acquire methods and attributes of another class is called:_____\nA. Inheritance \nB. Abstraction \nC. Polymorphism\nD. Objects")
ans_1 = input("eEnter your answer(A/B/C/D): ")
if ans_1 == "A":
    score += 1
    print("corect answer")
    print(f"your score is {score}/1")
else:
    print("Incorect answer")
    print(f"your score is {score}/1")
if ans_1 !="A":
    print(f"Answer is {ans_1}")

q_2 = print("Which of the following is a type of inheritance:____\nA. Single\nB. Double\nC. Multiple\nD. both A and B")
ans_2 = input("eEnter your answer(A/B/C/D): ")
if ans_2 == "C":
    score += 1
    print("corect answer")
    print(f"your score is {score}/2")
else:
    print("Incorect answer")
    print(f"your score is {score}/2")
if ans_2 !="C":
    print(f"Answer is {ans_2}")

q_3 = print("What is the depth of Multilevel inheritance in python:____\nA. Two level\nB. Three level\nC. Any level\nD. none of these")
ans_3 = input("eEnter your answer(A/B/C/D): ")
if ans_3 == "C":
    score += 1
    print("corect answer")
    print(f"your score is {score}/3")
else:
    print("Incorect answer")
    print(f"your score is {score}/3")
if ans_3 != "C":
    print(f"Answer is {ans_3}")

print("*********************************************************")
print(f"your total score = {score}")
f_score = (score/3)*100
print(f"percentage = {f_score}%")



