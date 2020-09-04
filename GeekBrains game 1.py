import random

number = random.randint(1,100)

user_number = None
count = 0
levels = {1: 10, 2:5, 3:3}

user_count = int(input('Enter quantity of players: '))
users = []
for i in range(user_count):
    user_name = input(f'Enter name {i}: ')
    users.append(user_name)

level = int(input('Choose level from 1 to 3: '))
max_count = levels[level]

is_winner = False
winner = None

while not is_winner:
    count += 1
    if count > max_count:
        print("You lose")
        break
    print(f'Try No {count}')
    for user in users:
        print(f'{user} enters number')
        user_number = int(input("Enter a number:"))
        if user_number == number:
            is_winner = True
            winner = user
            break
        elif number < user_number:
            print("Number is greater")
        elif number > user_number:
            print("Number is less")
else:
    print(f"Congrats, {winner}!")
