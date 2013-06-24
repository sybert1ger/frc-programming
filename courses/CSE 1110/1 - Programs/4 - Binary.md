---
title: Binary
layout: coursepage
---

You've probably heard a few times in your life that computers use 0's and 1's to do everything. You might not be sure how.

It's far more simple than you might assume.

Binary is a way of representing data - using 0's and 1's. Combinations of the two represent more complex data.

The standard way of representing data is by powers of 2. Don't be intimidated by this, it simply means that from right to left, the 0 or 1 is equivalent to 2^n.

So,

    0001

Means

    1 1
    0 2
    0 4
    0 8

or

    1 1's, 0 2's, 0 4's, 0 8's
    
or
    
    1

To keep things simple, just double the last value instead of using 2^n. It will always start at 1.

Another example would be:

    01010100
    
So, keep things simple. Go from right to left, starting at 1 and doubling each time

    0 1
    0 2
    1 4
    0 8
    1 16
    0 32
    1 64
    0 128

or

    0 1's, 0 2's, 1 4's, 0 8's, 1 16's, 0 32's, 1 64's, 0 128's

or

    4 + 16 + 64 = 84
    
The standard characters can be represented using only 8 places. Each number from 0 to 255 represents a different character.

8 places (or *bits*) is known as a *byte*. There are 1024 bytes in a kilobyte, 1024 kilobytes in a megabyte and 1024 megabytes in a gigabyte.

That's 1 073 741 824 bytes in a gigabyte! You can fit more than a billion characters in a gigabyte.

### Executables
Binary, when applied to executable programs, can become a huge mess. Thankfully, you don't need to worry about that at all. The libraries already developed makes the machine code irrelevant to programmers.

## Activity
For practise, find the value of these binary numbers:

    101010010101
    100101010010
    010101010010

And, write these numbers in binary format:

    1023
    1000
    221

Test your answers using [this](http://acc6.its.brooklyn.cuny.edu/~gurwitz/core5/nav2tool.html) tool.
