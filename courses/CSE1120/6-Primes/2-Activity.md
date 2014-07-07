---
title: Prime Numbers Activity
layout: coursepage
---

Place this code snippet at the bottom of a file.

    print('press enter for next prime')

    i = 0
    while(x == ''):
        i = next_prime(i)
        print(i)
        x = raw_input()

At the top of your code, create a `next_prime(x)` function that will return the next prime after `x`.

Run the program. You're output needs to match the following:

    3
    5
    7
    11
    13
    17
    19
    23

After pressing enter 8 times. Be sure your program will never output a number that is not a prime, and that no primes are missing. Use [this](http://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_500_prime_numbers) list as reference.

*Hint: try also making an `isprime(x)` method to modularise functionality.*
