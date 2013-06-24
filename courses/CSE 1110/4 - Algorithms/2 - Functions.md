---
title: Functions
layout: coursepage
---

So far, we've dealt with functions to a degree. Functions are one of the basic elements of a program.

We'll step back a little to get a good understanding of functions.

Think about how you would use a debit card to buy a chocolate bar. You might describe it like this:

    walk up to cashier
    tell them you are buying 1 chocolate bar
    insert card
    select account
    type pin number in
    remove card when done

The thing is, this can become cumbersome when buying things other times. You'll need to rewrite these instructions every time.

You can do something like this:

    define buy(item) as
        walk up to cashier
        tell them you are buying 1 'item'
        insert card
        select account
        type pin number in
        remove card when done

and buying a chocolate bar is as simple as:

    buy(chocolateBar())
    
Note that `chocolateBar()` creates a chocolate bar. `buy` will buy that bar.

What happens when you want to buy multiple chocolate bars? Try something like this:

    define buy(number, item) as
        walk up to cashier
        tell them you are buying 'number' of 'item'
        insert card
        select account
        type pin number in
        remove card when done

That way, you can buy 12 chocolate bars if you want.

*And*, you can simplify the first `buy` as.

    define buy(item) as
        buy(1, item)

This buys 1 of the item, without having to specify you're buying 1 every time.

# In Python
So how do we do this kind of thing in Python? It looks something like this:

    def buy(number, item):
        walkTo(cashier)
        say("I am buying " + str(number) + " of " + str(item))
        insertCard()
        select(account())
        type(pin())
        removeCard()

`number` and `item` are both referred to as *arguments*. These arguments are referable inside of the function.

`print` is also a function. It prints a string value to the console.

Remember, always make functions when you do things more than once.

Also note that you need to define a method before using it somewhere else (ex. don't call `foo()` before defining `foo()`)

# Returning
A function can *return* a value. This means that calling the function can be used as a value.

For example:

    buy(chocolateBar())

`chocolateBar()` returns a chocolate bar. This allows `buy` to actually buy the chocolate bar.

In a function, you return values using `return`.

    def chocolateBar():
        return ChocolateBar(1)

This function creates 1 `ChocolateBar` and returns it.
