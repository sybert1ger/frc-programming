---
title: Errors
layout: coursepage
---

Here, we will explain how to understand an error message in python and how to fix the error. Luckily, python has a high caliber error message generator. Typically it is very obvious what your error is. Other languages aren't so lucky.

Error messages are formatted in a consistent way. They will all follow this basic format:

    Traceback (most recent call last):
      Line 1, in <module>
          1 / 0
    ZeroDivisionError: integer division or modulo by zero

Let's examine each line of this error message.

    Traceback (most recent call last):

This is always included in error messages. It's simply an identifier that tells you that what proceeds was the place where the error occured. Traceback refers to "tracing our steps backwards". 

      Line 1, in <module>

This line tells you at which line the error occured, and in which file it occured. `<module>` can be replaced with the actual module's name. You haven't written multiple modules yet, but this can be important to know when you do.

          1 / 0
    ZeroDivisionError: integer division or modulo by zero

This tells you what went wrong, and where. In this example it's very clear. You've divided by zero, which is illegal. The second error starts with the error name, and then the message associated with that error.

# Common Errors
The most common exceptions are:

- SyntaxError - Python could not interpret the instruction. Typically this means you've tried to do something that you cannot.
- TypeError - You tried to do something with a variable with the assumption that the variable was a certain type, and it was not.
- NameError - You used a variable or method that doesn't yet exist.
- IOError - An error occured when using Input or Output

There are many other different error types, but these are the ones you will mostly deal with for now. It's easy to find out what an error means by looking it up in the python [documentation](http://docs.python.org/2.7/genindex-all.html) or google.

# Handling Exceptions
Python makes errors/exceptions very convenient. You can *raise* or *catch* an error. Let's explore these options.

Raising an exception/error is as easy as

    raise Expection('error message')

You can also specify which error it is.

    raise IOError('reading file failed')

You can also make your own error types.

    class MyException(Exception):
        def __init__(self, msg):
            self.msg = msg

You probably won't need to do this very often.

Catching an exception is done with something called a try-catch block.

    try:
         x = int(raw_input("Please enter a number: "))
    except ValueError:
         print "Oops!  That was no valid number.  Try again..."

You can also catch multiple exceptions.

    try:
         x += int(raw_input("Please enter a number: "))
    except (ValueError, NameError):
         print "Oops!  That was no valid number.  Try again..."

Or separetely

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error:", sys.exc_info()[0]

Remember that everything in an `except` block *only* runs when that error was raised inside of the `try` block. If no exceptions were thrown, no `except` blocks will run.
