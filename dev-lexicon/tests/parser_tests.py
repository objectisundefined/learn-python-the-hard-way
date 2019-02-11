from nose.tools import assert_equal, assert_raises
from app.parser import parse_sentence, ParserError

def test_parse_sentence():
  x = parse_sentence([('verb', 'run'), ('direction', 'north')])

  assert_equal(x.subject, 'player')
  assert_equal(x.verb, 'run')
  assert_equal(x.object, 'north')

  x = parse_sentence([
    ('noun', 'bear'),
    ('verb', 'eat'),
    ('stop', 'the'),
    ('noun', 'honey')
  ])

  assert_equal(x.subject, 'bear')
  assert_equal(x.verb, 'eat')
  assert_equal(x.object, 'honey')


def test_parse_error():
  assert_raises(ParserError, parse_sentence, [])


# assert_raises(exception, callable, parameters)