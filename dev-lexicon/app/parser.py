# ex49
# This will also work on longer sentences such as lexicon.scan("open the door and smack the
# bear in the nose").
# Now let us turn this into something the game can work with, which would be some kind of Sentence
# class. If you remember grade school, a sentence can be a simple structure like:
# Subject Verb Object

# Match and Peek
# To do this we need five tools:
# 1. A way to loop through the list of scanned words. That’s easy.
# 2. A way to “match” different types of tuples that we expect in our Subject Verb Object setup.
# 3. A way to “peek” at a potential tuple so we can make some decisions.
# 4. A way to “skip” things we do not care about, like stop words.
# 5. A Sentence object to put the results in.

class ParserError(Exception):
  pass


class Sentence(object):
  def __init__(self, subject, verb, obj):
    # remember we take ('noun','princess') tuples and convert them
    self.subject = subject[1]
    self.verb = verb[1]
    self.object = obj[1]


def peek(word_list):
  if word_list:
    word = word_list[0]
    return word[0]
  else:
    return None


def match(word_list, expecting):
  if word_list:
    word = word_list.pop(0)

    if word[0] == expecting:
      return word
    else:
      return None

  else:
    return None


def skip(word_list, word_type):
  while peek(word_list) == word_type:
    match(word_list, word_type)


def parse_verb(word_list):
  skip(word_list, 'stop')

  if peek(word_list) == 'verb':
    return match(word_list, 'verb')
  else:
    raise ParserError("Expected a verb next.")


def parse_object(word_list):
  skip(word_list, 'stop')
  next_word = peek(word_list)

  if next_word == 'noun':
    return match(word_list, 'noun')
  elif next_word == 'direction':
    return match(word_list, 'direction')
  else:
    raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
  skip(word_list, 'stop')
  next_word = peek(word_list)

  if next_word == 'noun':
    return match(word_list, 'noun')
  elif next_word == 'verb':
    return ('noun', 'player')
  else:
    raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
  subj = parse_subject(word_list)
  verb = parse_verb(word_list)
  obj = parse_object(word_list)

  return Sentence(subj, verb, obj)


# t = (1, 2)
# t[0] t[1]
