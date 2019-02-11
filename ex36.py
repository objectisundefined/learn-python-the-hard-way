# Rules for if-statements
# 1. Every if-statement must have an else.
# 2. If this else should never run because it doesn’t make sense, then you must use a die function
# in the else that prints out an error message and dies, just like we did in the last exercise. This
# will find many errors.
# 3. Never nest if-statements more than two deep and always try to do them one deep.
# 4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of
# sentences. Put blank lines before and after.
# 5. Your Boolean tests should be simple. If they are complex, move their calculations to variables
# earlier in your function and use a good name for the variable.from sys import exit

# Rules for Loops
# 1. Use a while-loop only to loop forever, and that means probably never. This only applies to
# Python; other languages are different.
# 2. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number
# of things to loop over

import random as r

def game():
  begin, end = 1, 10 + 1
  num = r.randint(begin, end)

  print(f"guess a integer in [{begin}, {end})")

  i = 0
  max_guess = 5

  while True:
    guess = input("> ")

    if guess.isdigit():
      guess_num = int(guess)
    else:
      print("Bad input. Game end!")
      return

    i = i + 1

    if num == guess_num:
      print(f"Great congratulations! You guessed {i} times.")
      return

    if i > max_guess:
      print(f"Sorry. You have guess more than {max_guess} times.")
      return

    print("Not right. Please try again!")

game()

# a number guess game