from sys import argv

# pylint: disable=unbalanced-tuple-unpacking
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# python3.7 ex13.py first 3nd 3rd
# variables unpacking
# script is default variable file when you run python file