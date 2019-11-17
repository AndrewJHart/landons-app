import random
import requests
import json
import re

# regex tag to remove simple html tags from the answers (borrowed from stack overflow)
TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    """
    Strips the given text parameter of most html tags and
    returns the string without html formatting

    :param text - the text with html to strip
    """
    return TAG_RE.sub('', text)


# make a http GET request to jservice questions JSON API for all clues with science category id of 25
response = requests.get('http://jservice.io/api/clues?category=25')

# convert the json string into a python array of dicts
data = json.loads(response.text)

print('--------------------------------')
print('          TIME TO QUIZ!         ')
print('--------------------------------')
print('When you want to exit, type EXIT')
print('--------------------------------\n')

name = input('Player, what is your name?')
print('')


while True:
    # generate a random number from 0 to length of array - 1
    the_number = random.randint(0, len(data) - 1)

    # retrieve question from array of questions using the random number as the index
    the_question = data[the_number]['question']

    # request user input for their answer to given question
    guess = input(the_question).lower()

    # format the answer, remove html tags, lower case it, and split it into array of words
    answer = remove_tags(data[the_number]['answer']).lower()

    # checking if the user wants to quit the program
    if guess == 'exit'or guess == 'quit':
        break

    # lower case the guess and see if its in the answer.. this resolves issues where an answer may
    # contain `an electron` but the user types `electron` which is correct but shows incorrect
    # so we split the string into array of words and simply check if the answer is any of those words.
    if guess in answer:
        print('Awesome, your answer is correct {0}! \n'.format(name))
    else:
        print('Sorry {0}, your answer was incorrect, it was {1} \n'.format(name, remove_tags(data[the_number]['answer'])))
        print('Try another question!\n')


print('\nGAME OVER\n')
