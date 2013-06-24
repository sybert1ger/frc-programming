---
title: Iteration
layout: coursepage
---

The usage of loops in math are powerful. But you have to ask "is that really it?". Well, considering we've asked the question, yes. The algorithm usage of loops is the tip of the iceberg. More often, programmers deal with *iteration*.

But before we can explain iteration, you have to know what we're actually *iterating* through.

There are 3 forms of things we will iterate through. In reality, there are more possibilities, but most use the same principles as these three.

## Dictionaries
Say you're trying to save the entire english dictionary in a program. You only need the word and its definition. How exactly would you go about doing that?

You might try storing every word as a new variable. It might work, but your program becomes enormous and unreadable. None of it makes any sense.

Maybe, there is a better solution conviniently named a "dictionary". This solution stores data in a way that is similar to a dictionary does. Every definition, or "element", is directly associated with a word, or "key".

A dictionary looks like this:

    words = {
        'word' : 'definition',
        'another word' : 'another definition'
    }

To the naked eye, this might seem even *worse* than making a new variable for each word. But it is surely not. Dictionaries come with some very powerful tools that make them much more dynamic and useful.

To access a word's definition, you would simply call:

    words['word']

The definition (element) is internally attached to its word (key).

As an added benefit, you can add, edit and remove entries in dictionary.

    # Add a word
    words['new word'] = 'new definition'
    # Edit a word
    words['word'] = 'different definition'
    # Removes a word
    del words['new word']

## Lists
What if we don't need a key? In that case, *lists* are useful.

Lists use a zero-based (starts at zero) index to access values. So instead of `word` as a way to access the definition, an index is used. For example:

    powersoftwo = [1, 2, 4, 8, 16, 32, 64]

You access the values using the index of the value.

    powersoftwo[0] # this is 2
    powersoftwo[4] # this is 16

To add elements to a list, use `append(element)` or `insert(index, element)`. Appending will insert the element at the end of the list, and inserting will insert the element at the specified index, pushing elements to the right.

## Tuples
You might not want to change a list. It might even be a requirement not to be able to. In that case, use tuples.

Tuples are almost equivalent to lists, except for the fact that they cannot be changed (*mutated*). This is good for performance and application reasons.

Create tuples using this notation:

    friends = ('bob', 'frank', 'stacy')

Both lists and tuples are capable of performing some useful operations. See [Data Structures](http://docs.python.org/2/tutorial/datastructures.html) for more information.

# Iteration
Alright, hopefully you have a basic understanding of some basic data structures. At this point, you probably have a hint of what's coming next. We want to *iterates through elements*.

We can do this with any of the three data types. Dictionaries are the least intuitive.

To iterate through a dictionary, you need to specify what you want to iterate through. This can either be the *keys* or *elements* or both.

To iterate through keys, use this notation:

    phones = {'frank' : 2332323, 'emily' : 1223131}
    for name in phones.keys():
        print(name)

This will print frank and emily's names. This is because the for loop will iterate through `phones.keys()`, and assign the values to `name` on each run through. `name` is different each time because the keys are different. Every iterating for loop uses this same mechanic. `name` has no significance other than being easy to read. It can be anything that is a valid variable name.

Dictionaries, unlike lists and tuples, have no predifined order. They will *not* be sorted in any particular way. Don't design programs that relies on their order.

You can iterate through the elements as well.

    for number in phones.values():
        print(number)

You can also iterate through both elements and keys at the same time.

    for name, number in phones.items():
        print(name + " is at " + str(number))

Iterating lists and tuples is much easier.

    list = ['element1', 'element2', 'element3']
    tuple = (1, 2, 3)

    for element in list:
        print element

    for number in tuple:
        print tuple

# Uses
Now that you know how to create and iterate through data, what can you use this for? Well, the uses are endless. You can have a selection of options for the user to choose through. Iterating through those values makes it easy to put them anywhere. For example, you might have a selection of ages.

    ('0-18', '19-23', '24-30', '30-40', '40-60', '60-80', '80+')

You can then use these values as possible selections for the user, and reference with age using one number (the index).

It's difficult to understand the power of what you're doing though. Some concepts of programming have a lot of uses, but are difficult to quantify as useful. Iteration of one of those. As long as you understand *how* to iterate, the potential of it will slowly reveal itself.
