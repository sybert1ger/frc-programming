---
title: Looping
layout: coursepage
---

You already know what a loop is. It's a pretty basic concept when you think about it. All the computer is doing is executing some instruction(s) more than once, based on a condition. You could even visualise a basic circuit that does this.

What you might not have a firm grasp on, however, is their application. Why in the world do we need to  do something more than once? It's not a bad question, actually. There's really no reason why we couldn't write programs without loops.

The problem is, they would look silly and insanely long. Imagine replacing this loop.

    for x in range(100):
        print(x)

If we were to imagine a language without loops, this loop would be [this](/resources/no-loops). You can guess why loops could be useful.

But you've only seen very rudimentary versions of loops. You haven't got the chance to see many of the useful looping mechanisms possible. Unfortunately, this is a consequence of the complexity of some of those things. Things like waiting are difficult to do. There are good reasons that many of the loops you use on a daily basis as a programmer are abstracted away from you. You rarely directly come into contact with the majority of loops. Be sure, however, that they are there.

We'll explore an example from the math function activity - factorials.

You (hopefully) used a form of loop to complete the task. This is because of the way that factorials work.

    N! = N * (N - 1) * (N - 2) * ... * (1)

You can almost immediately see where the loop comes in. There are clearly divided steps, each of which does almost the same operation.

Notice that N will never change. The only thing that changes from step to step is the result of N - I. We'll use I as an abbreviation of "index", referring to the index of the set.

Each step has an index. The first index is 0, and each step proceding is 1 larger than the previous one. So,

    N = Index 0
    N - 1 = Index 1
    1 = Index N

The last element (1) will be at index N because index starts at 0 and increments everytime until it hits zero (the Nth occurance/element).

So, we will run the loop until the index is equal to N.

    I = 0
    while I < N:
        I += 1

If you aren't familiar with what `+=` means, it is simply an abbreviation for `= I +`. It adds whatever is on the right side to the variable. This works for every operation.

So now we know how many times to run the loop. But how do we actually calculate the result?

We'll create a running total, called T.

    I = 0
    T = 1
    while I < N:
        I += 1
        T *= I

Notice that we use the index as a representation of the element. This simplifies our job.

This is a basic loop, but it provides an entire mathematical concept. Loops are very powerful.
