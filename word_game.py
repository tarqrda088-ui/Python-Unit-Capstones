import random
print("welcome to the word game")
word=("apple","banana","oranfe","grape")
word_random=random.randint(0,4)
secret_word=word[word_random]
first_letter=secret_word[0]
first_letters=input("enter the first letter of the word")
if first_letters==first_letter:
    print("first letter is correct")
else:
    print("first lettr is incorrect")

second_letter=secret_word[1]
second_letters=input("enter the second letterof the word")
if second_letter==second_letters:
    print("second letter is correct")
else:
    print("second letter is incorrect")

third_letter=secret_word[2]
third_letters=input("enter the third letter of the word")
if third_letter==third_letters:
    print("third letter is correct")
else:
    print("third letter is incorrect")

fourth_letter=secret_word[3]
fourth_letters=input("enter the fourth letter of the word")
if fourth_letter==fourth_letters:
    print("fourth letter is correct")
else:
    print("fourth letter is incorrect")

fifth_letter=secret_word[4]
fifth_letters=input("enter the fifth letter of the word")
if fifth_letter==fifth_letters:
    print("fifth letter is correct")
else:
    print("fifth letter is in correct")
