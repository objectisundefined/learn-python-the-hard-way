# ex48
# In our game we have to create a list of allowable words called a “lexicon”:
# • Direction words: north, south, east, west, down, up, left, right, back
# • Verbs: go, stop, kill, eat
# • Stop words: the, in, of, from, at, it
# • Nouns: door, bear, princess, cabinet
# • Numbers: any string of 0 through 9 characters

# from functools import reduce

directions = 'north, south, east, west, down, up, left, right, back'.split(', ')
verbs = 'go, stop, kill, eat'.split(', ')
stops = 'the, in, of, from, at, it'.split(', ')
nouns = 'door, bear, princess, cabinet'.split(', ')
numbers = "\\d+"

def tokenize(seg):
  if seg.isdigit():
    return 'number', int(seg)

  keywords_tuples = [
    ('direction', directions),
    ('verb', verbs),
    ('stop', stops),
    ('noun', nouns),
  ]

  for tag, keywords in keywords_tuples:
    for val in keywords:
      if seg == val:
        return tag, seg

  return 'error', seg


class Lexicon(object):
  def __init__(self):
    pass

  def scan(self, sentence):
    words = sentence.split(' ')

    # res = []
    # for word in words:
    #   res.append(tokenize(word))

    # return res

    # trnas iterable to list
    return list(map(tokenize, words))

lexicon = Lexicon()
