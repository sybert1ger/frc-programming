---
title: Consistency
layout: coursepage
---

Part of the fundamental definition of algorithms is consistency. Being able to provide the same output when given the same input is crucial. For example, this function is not consistent.

    def time(x):
        return getTime() * x;

Although the function takes input, returns output that is reliant on the input and is completely accurate, there is something seriously wrong. Don't get us wrong, this function could be useful, but it **is not a (stable) algorithm**. It not only outlines a strategy to make a decision, it does so based on something outside of our control.

**A stable algorithm run with input `x` will always return the same result, regardless of any other factor.**

Functions that aren't stable solve different kinds of problems. These problems have to do with state. Like the first example, they are reliant on some other part of the program, which has no predefined value. They are certainly useful in a lot of situations.

    def pow(x, y):
        return x ** y;

Algorithms are useful because of their consistency. You know that `pow(3, 2)` will always return the same value. You can rely on that fact, and therefore have no need to care about other parts of your code interfering with what you are doing.

A basic way to tell if a function is consistent is to check *if non-static values are used*. Static, in this case, meaning a value that can and will never change. (PI being a good example)

Remember that a consistent program is useful for programmers, users and computers. Knowing that your program operates consistently leaves some peace of mind.
