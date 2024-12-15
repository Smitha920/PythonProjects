import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
print("WELCOME TO PASSWORD GENERATOR👩‍💻")
n_num = int(input("how many digits you want in your password: "))
nl_letters = int(input("how many lower case letters you want in your password: "))
nu_letters = int(input("how many upper case letters you want in your password: "))
n_symbols = int(input("how many symbols you want in your password: "))
password = ""
for num in range(n_num+1):
    number = random.choice(numbers)
    password = password + str(num)
for letter in range(nu_letters+1):
    L_letter = random.choice(l_letters)
    password += L_letter
for letters in range(nu_letters+1):
    U_letter =random.choice(u_letters)
    password += U_letter
for sym in range(n_symbols+1):
    symbol = random.choice(symbols)
    password += symbol

print(password)