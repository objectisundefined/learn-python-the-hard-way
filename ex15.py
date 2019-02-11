from sys import argv

# pylint: disable=unbalanced-tuple-unpacking
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()

# reading files
# It's important to close files when you're done with them