---
title: Data Types
layout: coursepage
---

In programs, data is represented using a few different ways. This is because there are different things to represent. The main ones:

- Numbers
- Boolean Values
- Strings (Sequences of characters)

# Numbers
Numbers are represented in two main ways: Integers and Floats.

## Integers
Integers are whole numbers. They are useful for representing counts and amounts, but rarely good for calculations.

In python, you can explicitly declare or convert something as an integer using

    int(number)
    
Or, as long as the number does not have a decimal point, just use the number

    142

**Note**: Math with integers will always "floor" the result. This means that something like `5/2` would give you `2`, not `2.5`. Remember to use floats whenever there is a chance at non-whole number values.

## Floats
Floats are *floating point* numbers that represent decimal numbers. Remember, **floating point is not always perfectly accurate**.

In python, you can explicitly declare or convert something as a float using

    float(number)

Or, as long as the number has a decimal point, just use the number

    142.0

# Boolean Values
A Boolean is something true or false. Usually, they represent some kind of condition in the program. Something like `3 > 2`. This is true.

In python, you can explicitly declare something as a Boolean using

    bool(condition)

Usually, this isn't necessary.

You can also just use `True` or `False` if you know what the value is.

Python has support for all basic comparisons. They are all Boolean values:

`==` - Is Equal To

`!=` - Is Not Equal To

`>`  - Is Bigger Than

`<`  - Is Smaller Than

`>=` - Is Bigger Or Equal To

`<=` - Is Smaller Or Equal To

# String Values
A string is a sequence of characters put together. To tell python that something is a string (rather than being part of the program), use the `"` or `'` characters around them.

Example:

    "Hello"
    '15'

Note that `'15'` is not a number. Because there are quotes around it, it is a string.

Something like `Hello` is not a string. Python needs to be able to differentiate between normal programming and string values, so quotation marks are necessary.

You can combine strings together using `+`.

    "Hello " + 'World'

That is equivalent to:

    "Hello World"
    
Too convert any value to a string, use `str`:

    str(13)

Usually, user input is represented in strings. You will see a lot of usage of strings in programming.
