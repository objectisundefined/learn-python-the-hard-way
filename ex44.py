# there are three ways that the parent and child classes can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

# If both solutions solve the problem of reuse, then which one is appropriate in which situations? The
# answer is incredibly subjective, but I’ll give you my three guidelines for when to do which:
# 1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with
# it, then be prepared to know the class hierarchy and spend time finding where everything is
# coming from.
# 2. Use composition to package code into modules that are used in many different unrelated places
# and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code that fit under a
# single common concept or if you have to because of something you’re using.

class Foo(object):
  def __init__(self):
    print("before Foo __init__")
    # class Fzz(Foo, Bar), Foo first, this line is required
    # super(Foo, self) -> Bar
    # think scala traits
    super(Foo, self).__init__()
    self.fooTag = 'foo'
    print("after Foo __init__")

  def foo(self):
    print("call Foo.foo")


class Bar(object):
  def __init__(self):
    print("before Bar __init__")
    super(Bar, self).__init__()
    self.barTag = 'bar'
    print("after Bar __init__")

  def bar(self):
    print("call Bar.bar")


class Fzz(Foo, Bar):
  def __init__(self):
    print("before Fzz __init__")
    super(Fzz, self).__init__()
    print("after Fzz __init__")

  def act(self):
    self.foo()
    self.bar()


fzz = Fzz()
print(fzz.fooTag)
print(fzz.barTag)
fzz.act()

# mro: method resolution order
# or Fzz.mro()
print(Fzz.__mro__)
# (<class '__main__.Fzz'>, <class '__main__.Foo'>, <class '__main__.Bar'>, <class 'object'>)

class X(object):
  def f(self):
    print('x')


class A(X):
  def f(self):
    print('a')
  def extral(self):
    print('extral a')


class B(X):
  def f(self):
    print('b')
  def extral(self):
    print('extral b')


# class C(A, B, X):
class C(B, A, X):
  """
  class C(X, B, A):
  TypeError: Cannot create a consistent method resolution order (MRO) for bases X, B, A
  """
  def f(self):
    super(C, self).f()
    print('c')


# think scala traits


# The __mro__ attribute of the type lists the method resolution search order used by both getattr() and super().
# The attribute is dynamic and can change whenever the inheritance hierarchy is updated.

# There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.
# The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

# Inheritance versus Composition