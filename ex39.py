# create a mapping of state to abbreviation
states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI',
}

# create a basic set of states and some cities in them
cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
  print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
  print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


# name = 'lalala'
# stuff = {name: 'Zed'}

# print(stuff) -> {'lalala': 'Zed'}

# dict.items(...)
#   D.items() -> a set-like object providing a view on D's items

# dict.get(self, key, default=None, /)
#   Return the value for key if key is in the dictionary, else default.

# A dictionary is used to map or associate things you want to store to keys
# you need to get them. Again, programmers don’t use a term like “dictionary” for something that doesn’t
# work like an actual dictionary full of words, so let’s use that as our real world example.

# What if I need a dictionary, but I need it to be in order? Take a look at the collections
# .OrderedDict data structure in Python. Search for it online to find the documentation.

# if val is None: