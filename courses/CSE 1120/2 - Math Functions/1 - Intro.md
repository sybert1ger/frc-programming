---
title: Introduction to Math Functions Activity
layout: coursepage
---

Before doing the next activity, we need to go over some important concepts.

You might already be familiar with the first concept. You've already used it in programs. It is the fact that all instructions, including definitions, are *sequencial*. To understand this, lets look at a simple example.

    echo('hello')

    def echo(x):
        print(x)

    echo('world')

If you've programmed in a non-scripting language before, this might seem perfectly valid to do. But in python (and other scripting language), it is not. This is because `echo` is not defined before it is called. To python, `echo` doesn't exist yet. The second call of `echo('world')` is valid because it comes after `echo` is defined. Python will print this error when this program is run.

    Traceback (most recent call last):
      File "test.py", line 1, in <module>
        echo('hello')
    NameError: name 'echo' is not defined

The key is this:

    name 'echo' is not defined

`echo` hasn't been defined when `echo('hello')` is called. Python can't call something that doesn't yet exist. It would be dangerous for it to try and look later in the file for `echo`. So we're stuck with defining functions before calling them. This might seem like a large inconvenience right now, but you'll see that it is not.

The second concept you must be familiar with to create math functions is floating point arithmetic. Simply put, this is math for decimal numbers.

You won't always get exact answers with floats. For this reason, you need to account for the *edge cases*. Especially with money, the innacuracy can cost you.

For a full overview of floating point arithmetic, look at [this](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) article.

Input is done through `raw_input()`. Convert to int of float using `int(raw_input())` or `float(raw_input())`.

And one last thing before doing this activity: if you aren't familiar with the math concept given, explore more using google and [python math](http://docs.python.org/2/library/math.html). Be sure you try and *learn*, and not just copy-paste (we know it's tempting). Challenge yourself!
