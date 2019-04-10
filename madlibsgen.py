# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

from random import randint


def weekend(day):
    # your code here
    if day == 'Saturday' or day == 'Sunday':
        return True
    return False


print weekend('Monday')
# >>> False

print weekend('Saturday')
# >>> True

print weekend('July')
# >>> False


# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
     while n > 0:
        print n
        n -= 1
     print 'Blastoff!'


countdown(3)
# >>> 3
# >>> 2
# >>> 1
# >>> Blastoff!


# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def biggest(a, b, c):
    return bigger(a, bigger(b, c))


def median(a, b, c):
    if bigger(a, b) < biggest(a, b, c):
        return bigger(a, b)
    return c


print(median(1, 2, 3))
# >>> 2

print(median(9, 3, 6))
# >>> 6

print(median(7, 8, 7))
# >>> 7

print(median(11, 33, 22))
# >>> 22

print(median(4, 5, 6))
# >>> 5

print(median(8, 7, 7))
# >>> 7


# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes return
# the string "sofa" if the number is 0, else return "llama".


def random_noun():
    # your code here
    num = randint(0, 1)
    if num == 0:
        return 'sofa'
    return 'llama'


print random_noun()


# Write code for the function random_verb, which takes in no inputs but outputs
# one of two verbs randomly. Use the randint function to generate a number from 0-1
# and return a verb depending on whether the number is equal 0 or 1. Feel free to
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".


def random_verb():
    # your code here
    num = randint(0, 1)
    if num == 0:
        return 'run'
    return 'kayak'


print random_verb()


# Write code for the function word_transformer, which takes in a string word as input.
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB",
# return a random verb, else return the first character of word.


def word_transformer(word):
    # your code here
    if word == 'NOUN':
        return random_noun()
    if word == 'VERB':
        return random_verb()
    return word[0]


print word_transformer('NOUN')


# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

def process_madlib(mad_lib):
    processed = ""
    box_length = 4
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    i = 0
    while i < len(mad_lib):
       frame = mad_lib[i: i + box_length]
       to_add = word_transformer(frame)
       processed += to_add
       if len(to_add) == 1:
           i += 1
       else:
           i+=4
    return processed


    # print length


    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)

