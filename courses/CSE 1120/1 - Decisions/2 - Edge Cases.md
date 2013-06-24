---
title: Edge Cases
layout: coursepage
---

Now that you've developed an understanding of *decision making strategies*, how do we create them? There are millions of different decisions to be made in the world, with even more strategies possible for each. The possibilities are endless for how many ways to create a strategy to decide.

In engineering, an edge case is something that happens infrequently, or something a state of affairs which is at the boundaries of what is possible. Programming uses the term in a very similar way. To a programmer, edge cases are **low probability input**. For example, you wouldn't expect a user's response to "how old are you?" to be "AWIFHUSAD@@@". This answer is nonsense and makes no sense. The important thing to know, however, is that this input is *completely possible*.

Just the pure possibility of a situation makes it something you must account for. This does not, however, mean that you must always include every single possible situation in your decision making strategies. Your accounting for some sort of situation can very well be "let the program fail". This thinking is both useful and dangerous at the same time. It's certainly a valid strategy for some cases; you don't need to care about non-number ages. But if you ignore invalid input that isn't *intrinsically* wrong, you will start to see problems.

For example, 12030203 is a valid age. But in reality, it's surely not. Letting the user get away with such a blatant violation can be a huge problem. For example, later on, your program might do something that takes for granted that no one is over 140 years old. Or you might try to display the person's age to others, and the pure length of the number makes everything on the screen look disproportionate.

Accounting for edge cases is something that good programmers do by default. It's just part of the decision making.

    if age > 140 || age < 0:
        print "user age is wrong!"
    else:
        # Do whatever needed

This kind of accounting for is useful to keep the program from slowly becoming corrupt with invalid input. Its behaviour becomes unpredictable after something invalid has been given to it.

Notice that in the example, it checks for invalid input *before* continuing. Checking input after already using the input is just plain useless.
