import random

# Write your code here
index = 0
possible_choices = list()
user_ratings = dict()
user_score = 0
new_user = 'False'


def load_ratings():
    file = open('rating.txt', 'r')
    global user_ratings
    global user_name
    global user_score
    global new_user
    for item in file:
        if user_name == item.split()[0]:
            user_score = int(item.split()[1])
        else:
            new_user = 'True'
    count = 0
    for items in file:
        user_ratings[count] = {'name': items.split()[0], 'score': items.split()[1]}
        count += 1
    file.close()


def evaluate_game(user_choice_):
    global computer_answer
    global index
    global user_choice
    global user_score
    user_choice_index = possible_choices.index(user_choice_)
    computer_answer_index = possible_choices.index(computer_answer)
    if user_choice_ == computer_answer:
        print('There is a draw (' + computer_answer + ')')
        user_score += 50
    elif user_choice_index <= (len(possible_choices) - 1) / 2:
        if user_choice_index < computer_answer_index <= int(user_choice_index + ((len(possible_choices) - 1) / 2)):
            print('Sorry, but the computer chose ' + computer_answer)
        else:
            print('Well done. The computer chose ' + computer_answer + ' and failed')
            user_score += 100
    else:
        # user_choice_index > (len(possible_choices) - 1) / 2:
        if int(user_choice_index - (len(possible_choices) - 1) / 2) <= computer_answer_index < user_choice_index:
            print('Well done. The computer chose ' + computer_answer + ' and failed')
        else:
            print('Sorry, but the computer chose ' + computer_answer)
    computer_answer = random.choice(possible_choices)
    user_choice = input()


def rating_print():
    global user_score
    print('Your rating: ' + str(user_score))


def write_ratings():
    global new_user
    global user_score
    global user_name
    global user_ratings
    file = open('rating.txt', 'w')
    count = 0
    while count < len(user_ratings):
        if count != len(user_ratings) - 1:
            if user_name == user_ratings[count].get('name'):
                line = user_name + ' ' + str(user_score) + '\n'
            else:
                line = user_ratings[count].get('name') + ' ' + user_ratings[count].get('score') + '\n'
        file.write(line)
        count += 1
    line = user_name + ' ' + str(user_score)
    file.write(line)
    file.close()
    pass


user_name = input('Enter your name:')
print('Hello, ' + user_name)
load_ratings()
list_of_options = input()
print("Okay, let's start")
possible_choices = ['rock', 'paper', 'scissors'] if len(list_of_options) == 0 else list_of_options.split(',')
user_choice = input()
computer_answer = random.choice(possible_choices)
while user_choice != '!exit':
    if user_choice in possible_choices:
        evaluate_game(user_choice)
    elif user_choice == '!rating':
        rating_print()
        user_choice = input()
    else:
        print('Invalid input')
        user_choice = input()
write_ratings()
print('Bye!')
