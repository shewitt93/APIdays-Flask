# list3 = [1, 2, [3, 4, 'hello']]

# list3[2][2] = 'goodbye'

# print(list3)

# list4 = [5, 3, 5, 1, 2, 4, 3, 2]

# sorted(list4)

# list4.sort()

# print(list4)

# d = {'k1': [ 1, 2, {'k2': ['this', {'tough':[1, 2, ['hello']]}]}]}

# print(d['k1'][2]['k2'][1]['tough'][2])

# import random

# num = random.randint(1, 100)

# guesses = [0]


# while True:
    
#     guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
#     if guess < 1 or guess > 100:
#         print('OUT OF BOUNDS! Please try again: ')
#         continue
    
#     if guess == num:
#         print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
#         break
   
#     guesses.append(guess)
  
  
#     if guesses[-2]:  
#         if abs(num-guess) < abs(num-guesses[-2]):
#             print('WARMER!')
#         else:
#             print('COLDER!')
#     else:
#         if abs(num-guess) <= 10:
#             print('WARM!')
#         else:
#             print('COLD!')