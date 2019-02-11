i = 0
numbers = []

while i < 6:
  print(f"At the top i is {i}")
  numbers.append(i)

  i = i + 1
  print("Numbers now: ", numbers)
  print(f"At the bottom i is {i}")

print("the numbers: ")

for num in numbers:
  print(num)

# while loops

# What’s the difference between a for-loop and a while-loop? A for-loop can only iterate
# (loop) “over” collections of things. A while-loop can do any kind of iteration (looping) you
# want. However, while-loops are harder to get right, and you normally can get many things
# done with for-loops.