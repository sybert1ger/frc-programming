---
title: Algorithms
layout: coursepage
---

For the sake of understanding, let's learn about algorithms by looking at a specific example: Bubble sort.

### The problem
We are given a list of numbers, in any random order. We are given the task of organizing these elements in an ascending order.

So we have an **input**: a list of numbers (we'll call this `list`). And we have an **output**: a sorted list of numbers.

### Solving the problem
Let's look at what we know already:

    function bubblesort takes input of 'list':
        ; sort the elements
        return 'list'

Basically, we're saying that the `bubblesort` function takes a list, puts the elements in correct order and returns the list back.

How do we organize the elements? Let's start with a loop.

**From here on out, we are only showing the "sorting" section of the function** - don't worry about the top for now.

    for all elements in 'list':
        ; do something with the element

To eventually get elements sorted, we'll need to compare them to each other. We can use the `<` (less than) symbol to compare.

    for all elements in 'list':
        if current element is < last element:
            swap elements

We should swap the elements because we want ascending order.

Does this function work yet? Not quite. All elements are not sorted, only one swap is performed. We need to keep going until we know that everything is sorted correctly.

    until not_sorted is false:
        not_sorted = false
        for all elements in 'list':
            if current element is < last element:
                swap elements
                not_sorted = true

Alright, we added a bit there. In reality, it's quite simple. If a swap is performed, that means we have no guarantee that the list is sorted. We make `not_sorted` true because we want to go through the list again to make sure everything is correct. We reset `not_sorted` to false every time we go back to the beginning of the list.

This function, in python, would look like:

    sorted = False
    while not sorted:
        sorted = True
        for x in range(1, len(list)):
            if list[x] < list[x - 1]:
                prev = list[x-1]
                list[x-1] = list[x]
                list[x] = prev
                sorted = False

Don't worry if you don't understand exactly what's going on, it's exactly the same as the previous pseudo code.

Let's put everything back into our function.

    function bubblesort takes input of 'list':
        until not_sorted is false:
            not_sorted = false
            for all elements in 'list':
                if current element is < last element:
                    swap elements
                    not_sorted = true
        return 'list'

So what did we learn?

## The algorithm
An algorithm is given an input, and returns an output. It will always (for our purposes) return the exact same output for a given input. In essence, this means that giving a list of `[2, 1, 4, 3]` will always return `[1, 2, 3, 4]` from our bubblesort algorithm.
