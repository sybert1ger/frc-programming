---
title: Parsing
layout: coursepage
---

What does a computer do when you give it a number? Well, to the user it appears that the number is automatically interpreted. Does the computer 'just know' when you're giving it a number?

No, it absolutely doesn't. We've had to deal with this in a few programs. If you want a number, you might use

    int(raw_input())

or

    float(raw_input())

You might have used this technique. It's useful because python has this functionality built in. But what isn't revealed is what's actually happening here. It's something known as **parsing**. Parsing is actually one of the more important concepts in computer programming. Without it, a lot of our programs wouldn't function.

Don't confuse parsing with conversion. We aren't simply converting a string value to a number. Let's explore what `int()` does.

So we have the string `'1320'`. We need to examine it and find out what number is represented. But where to start?

The simplest way to examine the number is by going number by number.

    for char in '1320':

So what do we do with each character? We find out what number it is. Lets simplify our job using a method.

    def tonum(char):
        if char == '0':
            return 0
        elif char == '1':
            return 1
        elif char == '2':
            return 2
        elif char == '3':
            return 3
        elif char == '4':
            return 4
        elif char == '5':
            return 5
        elif char == '6':
            return 6
        elif char == '7':
            return 7
        elif char == '8':
            return 8
        elif char == '9':
            return 9

And with this, we can convert every character to a number.
    
    for char in '1320':
        num = tonum(char)

Let's make a running total and an index.

    total = 0
    index = 0
    for char in '1320':
        index += 1
        num = tonum(char)

Remember that the decimal number system works using base-10. So 1320 means:

    1 1000
    3 100
    2 10
    0 1

Notice that each step is equal to 10^n. The first step (index 0) is 10^0. The second step (index 1) is 10^1. And so on.

So, we can use this property in our function.
    
    string = '1320'

    total = 0
    index = len(string)
    for char in string:
        index -= 1
        num = tonum(char)
        total += num * (10 ** index)

Notice that we've switch index to start at the end of the string and decrease every loop. This is because we're starting with the highest power and going down to 10^0.

And with this, we can parse any base-10 whole number. For an example of this program, look [here](http://codepad.org/c4gycedO). It will work no matter what input is given. But it *will* fail when the input is not a number.

In the official python implementation, parsing is done a little differently. This is for performance reasons. You should regard this code as a learning tool rather than something useful in the real world.
