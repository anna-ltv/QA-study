# Человек загадывает число, записывает его на бумаге
import random

min_number = 1
max_number = 100
user_answer = None

while user_answer != '=':
    number = random.randint(min_number,max_number)
    print(number)
    user_answer = input('Enter >, < or =: ')
    if user_answer == '>':
        min_number = number + 1
    elif user_answer == '<':
        max_number = number - 1
print("Computer wins!")
