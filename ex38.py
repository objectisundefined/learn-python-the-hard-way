class Thing(object):
  def test(self, message):
    print(message)

a = Thing()
a.test("hello")

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print("Adding: ", next_one)
  stuff.append(next_one)
  print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!

# A list is an ordered list of things you want to store and access randomly or linearly by
# an index

# What does stuff[3:5] do? That extracts a “slice” from the stuff list that is from element 3 to
# element 4, meaning it does not include element 5. It’s similar to how range(3,5) would work.
# '#'.join("a b c d e f g".split(' ')[3:5]) -> "d#e"