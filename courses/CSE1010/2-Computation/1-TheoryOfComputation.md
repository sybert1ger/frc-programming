---
title: Theory of Computation
layout: coursepage
---

The theory of computation involves a variety of subsets. For this course, we will look at two main ideas in computation - computability and computational complexity.

### Computability
The basic question of computability is "can this problem be solved by a computer?" In essence, we are asking how and if a specific problem can be solved given any valid input.

It's easy to quickly delve into the specifics and mathematics of computability, as there isn't much to say otherwise about solving problems. But we don't want to confuse you yet. Let's examine an example problem.

    Find the sum of 10 different numbers, all ranging from 1..200 and real whole numbers.
    
Seems easy enough, right? It is, and can be understood well.

Provided you have a computer with the aspects of a [Turing Machine](http://en.wikipedia.org/wiki/Turing_Machine), or in other words can deal with any kind of basic computation, this problem is solvable. This is because you have a way to add, and can keep a "running total" of the result. For example:

    define sum as 0
    for all numbers within 1 and 200:
        add number to sum

After this pseudo program has run, `sum` will have been defined as the sum of all numbers within 1..200

In essence, we are talking about reducing any problem into simple instructions. The last problem could be reduced into only addition.

### Computational Complexity
This is where things get interesting. First, let's define some terms:

An **algorithm** is a set way of solving a given problem, with adjustable input. Basically, it is a function capable of given output for an input.

**Big O notation** is the way of defining complexity. Simply put, it will tell us how long an algorithm takes. If the time is dependant on the input, Big O will use `n` as a way to say that it is related to the input of the function.

Let's use the previous function as an example:

    define sum as 0
    for all numbers within 1 and 200:
        add number to sum

Let's make 200 into an unknown variable, and call it `n`. And wrap this entire function as `sum`.

    function sum(1..n):
        define sum as 0
        for all numbers within 1 and n:
            add number to sum
        return sum

Now we have a proper function to evaluate. This function is an algorithm.

#### Big O
This is a relatively easy function to understand in Big O notation. Essentially, it will take `n` amount of steps. This is because we are adding numbers up until `n` - `n` amount of times.

You can imagine this using an example, given that `n` is defined as `5`. Our function would do the following.

    define sum as 0
    add 1 to sum    ; sum is now 1
    add 2 to sum    ; sum is now 3
    add 3 to sum    ; sum is now 6
    add 4 to sum    ; sum is now 10
    add 5 to sum    ; sum is now 15
    return sum

Essentially, we are taking 5 steps. You can ignore the reasonably simple steps, as they will become negligible very quickly (literally nanoseconds).

So we would define our function using Big O notation as *`O(n)`*. This means that it will take `n` steps to complete (in simple terms).

<iframe title="YouTube video player" class="youtube-player" type="text/html" width="640" height="390" src="http://www.youtube.com/embed/Ou2A-JWszVA"frameborder="0" allowFullScreen></iframe>

Sorting algorithms are interesting because you can compare many different ways of completing the same task.

![](http://algs4.cs.princeton.edu/25applications/images/sort-characteristics.png)

### P vs. NP
We won't delve too deep into this problem, as computer scientists are still not decided about the answers. But P and NP are still good topics to understand at a basic level.

**P** Problems are problems which result in `O(P)` complexity, or in other words, runs in *polynomial time*.

**NP** Problems are problems which the complexity is unknown or unsolvable. A computer may be able to solve these problems, but with no certainty of complexity. Most of the time, these solutions are easily verifiable.

Example problems:

####P
- Test if a number is prime

####NP
- Find the factors of any integer
- The travelling salesman problem (TSP) asks the following question: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?
