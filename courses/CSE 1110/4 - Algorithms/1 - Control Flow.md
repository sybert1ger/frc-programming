---
title: Control Flow
layout: coursepage
---

Sometimes you need to account for multiple situations inside of a program. Inside of a recipe, this might look like this:

    Add flour
    If dough is too dry, add 1 tablespoon of water
    ...
    Bake until fully risen

There are two conditions going on here. The first of which is `dough is too dry`. This condition is tested by the baker, and something is done in response to this.

The second condition is `fully risen`. The baker waits until this condition is true.

Both of these conditions seem very primitive and intuitive to a person. These types of instructions are common in computers.

In a computer, the instructions look like this (in python syntax):

    add(flour(1))
    if(dough.isDry()):
        add(water(1))
    ...
    while(not risen()):
        bake()
    stopBaking()

There are a few things to explain in this example.

- `add` adds an ingredient
- `flour(1)` creates 1 serving of flour
- `dough.isDry()` tests if `dough` is actually dry
- `water(1)` creates 1 tablespoon of water
- `risen()` checks if the cake is risen

You'll notice that this example makes it easy to adjust and change instructions. It can be much easier to do powerful operations in programming versus English.

One note as well - in `if` or `while` statements, the things to do are **indented**.

# Cases
There are some very useful and versatile things you can do with this kind of simple control flow. You probably don't even realise how powerful this is.

If you have a situation where there are a bunch of different cases possible, you can do so easily.

    x = 15
    
    if x < 5:
        print('x is less than 5')
    elif x < 10:
        print('x is less than 10')
    elif x < 15:
        print('x is less than 15')
    elif x < 20:
        print('x is less than 20')
    elif x < 25:
        print('x is less than 25')
    else:
        print('x is >= 25')


`elif` stands for `else if`.

You'll notice the `elif` statements in this code example take for granted that the conditions before them are false. The program goes over each statement sequentially, stopping if one of them is true. Like this:

    check condition
    if the condition was true, run the instructions inside of the condition
    if the condition wasn't true, test the next condition

So by effect, the `elif` means that the conditions before it weren't true.

You'll also notice the `else` statement only occurs once. This means that *none of the other conditions were true*. So in effect, x is more than or equal to 25.

# Loops
Loops are instruction that can be run more than one time, without coding it multiple times.

## While loops
The most useful loop is the while loop. It runs *while a condition is true*.

    x = 0
    while(x < 10):
        x = x + 1

So this will add 1 to `x` every time in the loop. At some point, `x` will be equal to 10, and `x < 10` will no longer be true. The program will then finish the loop and continue on to the next set of instructions.

## For loops
Python has special *for loops*. Generally, if you can express an instruction like `for something in something else`, python for loops work well.

    for x in range(10):
        print(x)

This will print numbers between 0 and 9. `range(x)` gives a range of numbers from 0 to `x`.

Although python has very powerful for loops, the range loop should be the only way you'll use it for now.
