# Ashton Wood
# 03-31-2023
# WhileLoopPractice
# While loop that tests for 5 in a range of 10 starting from 0

guess_me = 5
for number in range(10):
    if number < guess_me:
        print(number, 'is too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break

