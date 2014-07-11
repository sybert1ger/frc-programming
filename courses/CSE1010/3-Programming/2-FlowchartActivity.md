---
title: Flowchart Activity
layout: coursepage
---

Flowcharts are a simple way to essentially describe what a program does, in a visual way.

Let's illustrate the program from the "Theory of Computation" page.

    define sum as 0
    for all numbers within 1 and 200:
        add number to sum

![](/img/flowchart_activity.svg)

There are more rigorous ways to define flowcharts, with much more details and more specific diagrams. For an example traditional flowchart, see [here](http://www.programiz.com/article/flowchart-programming).

We won't be strict about how you format your flowchart, since the idea of using flowcharts is to illustrate concepts. If you can effectively do that, it shouldn't matter how it's done.

To complete this activity, use [Gliffy](http://www.gliffy.com/) to illustrate the following program.

    for all numbers within 1 and 10 (define as X):
        for all numbers within 2 and (X-1) (define as U):
            if X is divisible by U:
                print X is not prime

For those familiar with basic programming, see the python equivalent.

    for x in range(1, 11):
        for u in range(2, x):
            if x % u == 0:
                print x, "is not prime"
                break

Something worth noting about this program is that it is in no way definitive about prime numbers. For example, 1 is technically not prime. This program simply tests if there is a factor of the number that is over 2 and not itself.
