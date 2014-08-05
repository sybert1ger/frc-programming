---
title: Repetition as a Problem Solver
layout: coursepage
---

Now that you have a firmer grasp of repetition, you can start to solve much more complicated problems. Let's explore something called a *sorting algorithm*. We'll be using *bubble sort*.

Imagine you have a classroom full of kids. Everyone has a math grade. You want to look at comparisons between students, but everyone is inserted in random locations. Sure, you could compare two students and compare the numbers directly. But you don't have any context about the rest of the class. Where do the two fit in comparison to the entire class?

"I should sort them by grade", you say. "Then I can see where they fit inside of the class".

As you can imagine, this problem has been around for a long time in computing. People want information to be readable and in order. It's a natural need.

Think about how you might do this on paper. You have a list of students with grades.

    Lisa: 70
    Frank: 83
    Bill: 99
    Julia: 76
    Adam: 92
    Sophie: 60
    Chris: 88

You look at the list, and go one by one. Comparing with the next number. If they are in the wrong order, switch them.

    70 < 83 ? Yes. (Don't do anything)
    83 < 99 ? Yes.
    99 < 76 ? No. (Switch them)
    99 < 92 ? No.
    99 < 60 ? No.
    99 < 88 ? No.

So now you have a slightly better version.

    Lisa: 70
    Frank: 83
    Julia: 76
    Adam: 92
    Sophie: 60
    Chris: 88
    Bill: 99

What if you restart from the beginning and do the same thing?

    70 < 83 ? Yes.
    83 < 76 ? No.
    83 < 92 ? Yes.
    92 < 60 ? No.
    92 < 88 ? No.
    92 < 99 ? Yes.

And you end up with an even better version.

    Lisa: 70
    Julia: 76
    Frank: 83
    Sophie: 60
    Chris: 88
    Adam: 92
    Bill: 99

As you can imagine, you would continue to do this until it's fully sorted. Is this the best way? No, almost certainly not. There are easy performance tweaks that can make this function much better. But, that is not the element of focus here. Our goal is to make something useful for sorting. Adding extra instructions and conditions simply distracts us from accomplishing the goal. Leave the optimization to experts, at least for now.

So now that we have a method to sort elements, how do we do it inside of a program? First, let's construct the list of students.

Remember that we use a list, not a dictionary, because the order is important (dictionaries cannot define order).

    items = [
        ('Lisa', 70),
        ('Frank', 83),
        ('Bill', 99),
        ('Julia', 76),
        ('Adam', 92),
        ('Sophie', 60),
        ('Chris', 88)
    ]

Remember how to iterate through this list?

    for student in items:
        name = student[0]
        grade = student[1]

But with this we have no way to access the next element in the list. We need to do this because we're comparing the two.

So we need to opt for a solution that provides access to the current index.

    for index in range(0, len(items) - 1):

`len` just returns the length of the list. Notice that we use `len(items) - 1`. This is because we don't need to compare the last element with anything. There is no element after the last element.

So now we can take for granted the placement of both elements to compare.

    for index in range(0, len(items) - 1):
        grade0 = items[index][1]
        grade1 = items[index + 1][1]

Notice that we put `[1]` after both items. This is because `items` contain 2-element lists, with the name and key. For now, we don't care about the person's name. We only care about the grade.

So we compare the two grades.

    for index in range(0, len(items) - 1):
        grade0 = items[index][1]
        grade1 = items[index + 1][1]
        if grade1 < grade0:
            # switch them

So we need to switch the elements in the list. 

    a = items[index]
    b = items[index + 1]

    items[index] = b
    items[index + 1] = a

We can use the shorthand for this:

    items[index], items[index + 1] = items[index + 1], items[index]

So our method looks like this.
    
    for index in range(0, len(items) - 1):
        grade0 = items[index][1]
        grade1 = items[index + 1][1]
        if grade1 < grade0:
            items[index], items[index + 1] = items[index + 1], items[index]

But this will only go through our list once. Remember that we need to repeat this process until it is completely sorted. How do we check if the list is sorted? How about checking if any modifications were needed? If a change was needed, we don't know if the list is sorted yet. So,

    mod = False
    for index in range(0, len(items) - 1):
        grade0 = items[index][1]
        grade1 = items[index + 1][1]
        if grade1 < grade0:
            items[index], items[index + 1] = items[index + 1], items[index]
            mod = True

And we can do the entire function inside of a while loop.

    mod = True
    while mod:
        mod = False
        for index in range(0, len(items) - 1):
            grade0 = items[index][1]
            grade1 = items[index + 1][1]
            if grade1 < grade0:
                items[index], items[index + 1] = items[index + 1], items[index]
                mod = True

It's important to set `mod` to true at the start because otherwise the loop would never run. And it's also important to set `mod` to false at the beginning of every loop because otherwise it will always be true and never end.

So, let's test our sorting function.
    
    items = [
        ('Lisa', 70),
        ('Frank', 83),
        ('Bill', 99),
        ('Julia', 76),
        ('Adam', 92),
        ('Sophie', 60),
        ('Chris', 88)
    ]

    print 'BEFORE SORTING'
    print items

    mod = True
    while mod:
        mod = False
        for index in range(0, len(items) - 1):
            grade0 = items[index][1]
            grade1 = items[index + 1][1]
            if grade1 < grade0:
                items[index], items[index + 1] = items[index + 1], items[index]
                mod = True

    print 'AFTER SORTING'
    print items

The output of this program is [here](http://codepad.org/UKFBEe6J). You'll notice that the list is perfectly organized.

Of course, this method can be used for any list of students with grades. As a matter of fact, any list with a number as the second element can be sorted using this method.

Let's create a function out of our algorithm.

    def sort(items):
        mod = True
        while mod:
            mod = False
            for index in range(0, len(items) - 1):
                grade0 = items[index][1]
                grade1 = items[index + 1][1]
                if grade1 < grade0:
                    items[index], items[index + 1] = items[index + 1], items[index]
                    mod = True
        return items

We return `items` just for convenience, there's no real need for it.

And now we can call this method with any list of students.

    secondstudents = [
        ('Dylan', 54),
        ('Cassie', 87),
        ('Rick', 86),
        ('John', 40),
        ('Lisa', 70),
        ('Frank', 83),
        ('Bill', 99),
        ('Julia', 76),
        ('Adam', 92),
        ('Sophie', 60),
        ('Chris', 88)
    ]

There's obviously no order in this list, but calling `print(sort(secondstudents))` prints this:

    [('John', 40), ('Dylan', 54), ('Sophie', 60), ('Lisa', 70), ('Julia', 76), ('Frank', 83), ('Rick', 86), ('Cassie', 87), ('Chris', 88), ('Adam', 92), ('Bill', 99)]

The list is sorted!

We're using repetition a lot here. There is quite a bit of dynamic flow that allows the list to be sorted. We have a while loop that tests if the list is sorted, a for loop that iterates over elements and an if statement that compares elements. All of these different instructions combine to be something extremely useful. Not only is it useful for obvious things like data (think spreadsheets), it is also used in many internal parts of applications. For example, your computer's process manager uses dynamic sorting of processes to determine what programs to run when. 
