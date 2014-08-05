---
title: Syntax
layout: coursepage
---

One of the most common mistakes done by new programmers are syntax errors. It is typically because of inexperience. If you were to forget how exactly to perform some action, you would likely make a  syntax error.

Python is not ideal when catching syntax errors. Unfortunately, you will only know if your script has a syntax error when running the program. Thankfully there are tools (such as IDEs) that will find these errors before running. If you aren't using one of these tools, you will need to know how to fix syntax errors.

**An example syntax error**

    File "<stdin>", line 1, in ?
        while True print 'Hello world'
                       ^
    SyntaxError: invalid syntax

You'll notice that syntax errors are clearly labeled. This is helpful if you don't recognize your mistake. It lets you know exactly where python could not continue.

In this case, the error is that there was no colon after `while True`. Python didn't know what `print` meant because it thought it was still part of the condition for `while`.

## Common Syntax Errors
One of the most common syntax errors is the error we just looked at. Forgetting colons or indentation are errors that can break programs. Remember that blocks (if, while, for, class, def, etc.) *need* to contain some kind of code within them (indented). If you don't want anything to happen, use the keyword `pass`.

    if condition:
        # Do something
    else:
        pass; # Just move along

Another common syntax error is type names. For reference:

- Integers - `int`
- Floats - `float`
- Characters - `chr`
- Strings - `str`
- Booleans - `bool`

There are more types, but these are the most common.

One last common syntax error is the difference between dictionaries, lists and tuples. Remember that:

**Dictionaries**

    {
        key: item,
        key1: item1
    }

**Lists**

    [
        item,
        item1
    ]

**Tuples**

    (
        item,
        item1
    )

Dictionaries are unordered and use keys, lists use indexes, are ordered and mutable (can be changed), and tuples use indexes, are ordered and immutable (cannot be changed).
