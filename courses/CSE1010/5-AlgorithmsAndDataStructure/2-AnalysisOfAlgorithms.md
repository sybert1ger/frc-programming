---
title: Analysis of Algorithms
layout: coursepage
---

As you learnt in [Theory of Computation](/courses/CSE1010/2-Computation/1-TheoryOfComputation/), complexity can be measured by "steps".

Let's look at our example bubblesort algorithm, and compare it to similar algorithms.

For the sake of counting steps, we'll use the python example.

    sorted = False
    while not sorted:
        sorted = True
        for x in range(1, len(list)):
            if list[x] < list[x - 1]:
                prev = list[x-1]
                list[x-1] = list[x]
                list[x] = prev
                sorted = False

<table class="table">
<tr><td>Worst case performance</td><td>O(n^2)</td></tr>
<tr><td>Best case performance</td><td>O(n)</td></tr>
<tr><td>Average case performance</td><td>O(n^2)</td></tr>
</table>

Bubble sort is very inefficient for large n values. This is because there are (n-1) comparisons to do, many times. If the list is organized poorly, this has an even greater effect. Essentially, the performance of bubble sort is poor because a lot of unnecessary comparisons are made simply because of the way it works.

Bubble sort is not a commonly used algorithm in industry. It is only good if you have small lists, and want something simple to implement. It's one advantage is it's best-case performance. This is because of the fact that a perfectly sorted array will not do any extra work.

Exponential complexity is dangerous, and logarithmic or linear is always preferred. Almost never is n^2 favourable.
