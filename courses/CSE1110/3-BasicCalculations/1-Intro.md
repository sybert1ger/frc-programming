---
title: Intro to Basic Calculations
layout: coursepage
---

You will be doing an activity that will show you how to do some basic calculations using python.

# Math Functions
Python supports addition, subtraction, multiplication and division.

    print(3 + 3)
    print(2 - 13)
    print(12.8 * 102)
    print(132 / 11.2)

It also supports parentheses to force order of operations.

    print(3 * (2 + 4))

# Modulus
The only thing that might come as a surprise in python math is the modulus operator. It returns the "remainder" from the division.

    print(5 % 2)
    
That will print 1, because 5 / 2 is 2 R 1.

Modulus is different from division however, because it only gives the **remainder**.

A useful application of modulus is in time.

    minutes = 120302
    
    hours = int(minutes / 60)
    minutes = minutes % 60

This lets you ignore all of the hours that have already happened. You *could* do it this way as well without modulus.

    minutes = 120302
    
    hours = int(minutes / 60)
    minutes = minutes - (hours * 60)

They both do the same thing, but the first solution is faster to calculate since it is one less step.
