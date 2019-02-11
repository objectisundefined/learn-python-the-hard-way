print(3 != 4 and not ("testing" != "test" or "Python" == "Python"))

# False

# "test" and "test" -> "test"
# 0 and 1 -> 0

# Is there any difference between != and <>? Python has deprecated <> in favor of !=, so use !=.
# Other than that there should be no difference.
# 0 <> 1 works in python 2.7, but raise error in python 3.7

# Isn’t there a shortcut? Yes. Any and expression that has a False is immediately False, so you
# can stop there. Any or expression that has a True is immediately True, so you can stop there.
# But make sure that you can process the whole expression because later it becomes helpful.