---
title: Statements as Decisions
layout: coursepage
---

You already know how real world decisions are made. You make them all the time. "What should I eat for supper?", you might ask yourself. The process that your brain goes through to interpret and make a decision is inherent in your neural networks. Inside of your own mind, you *decide*.

    Question: What should I eat for supper?
    Qualifications: Time until supper, What I feel like, Funds to buy supper
    Process:
        If I don't have any time until supper, go out to eat.
        If I have more than enough money to go out, go out to eat.
        If I don't have enough money,
            If I have enough time / resources to make what I feel like, make that.
            If I don't have what I need, make something simple.

This entire process is obscured from our main conscientiousness. We don't have to go through this entire process outright in order to make the decision. You depend on your "background processing" to tell you what decision was made. This is the reason you often make decisions for seemingly no reason. In fact, there is a reason - you just weren't aware of the process.

What if you *were* aware of this process then? What if you had to manually manufacture every one of these decisions?

The answer is: You'd be **programming**. This manufacturing of decision making is exactly what programming is, at a basic level.

So although you might find it exhaustive to see problems in this way - step by step - it is intuitive to what human beings do on a daily basis. You just need to frame problems in a way that achieves goals.

# Decisions
The *if statement* is the fundamental building block that decisions are made from in programming. You can certainly frame any human decision using if statements. Consider the problem of what to eat:

    if timeUntilSupper() < timeToMakeSupper():
        goOut()
    elif money() > moneyToGoOut():
        goOut()
    else:
        if timeUntilSupper() >= timeToMakeSupper(myPreference()):
            make(myPreference())
        else:
            make(simpleSupper())
            
Here is the definition of each function used here:

- `timeUntilSupper()` - Calculates time remaining until suppertime
- `timeToMakeSupper()` - Calculates the minimum amount of time to make any meal
- `timeToMakeSupper(meal)` - Calculates the amount of time to make `meal`
- `goOut()` - Tells person to go out to eat
- `money()` - Amount of money available to dispense
- `moneyToGoOut()` - Calculates cost of going out
- `myPreference()` - Calculates what the user would prefer as a meal
- `make(meal)` - Tells the person to make `meal` at home

You'll notice that there is something new going on in this statement as well. There is an `else` statement that goes into a completely new `if` statement. This concept is known as *nesting* statements. It allows you to have deeply specific conditions without repeating things constantly. Everything indented in python is considered part of that *block*. The `else` block contains an entire `if-else` statement.

# Statement as a Decision
So how is a statement considered a decision? Let's look at one particular example from our previous problem:

    if timeUntilSupper() >= timeToMakeSupper(myPreference()):
        make(myPreference())
    else:
        make(simpleSupper())

This, in itself is not a decision. What it is, though, it a **strategy for deciding**. This means that you can make decisions using this strategy. You'll need to start changing how you think of programs. Almost no real-life program is designed as a *decision making mechanism*. What they do is much more elegant. Programs define ways to make decisions, and **let the user give the necessary input to make the decision**.

In our example, the user input is `myPreference()`. The result of the decision is dependant on that input.

You'll notice that we don't apply any *direct* tests to `myPreference()`. This is important, because input is not only defined by being tested. Input is just *something* that can change the outcome, depending on what it is. In this case, `myPrefence()` changes `timeToMakeSupper(myPreference())` and thus affects the condition `timeUntilSupper() >= timeToMakeSupper(myPreference())`. The condition's result is indirectly related to the input. Input can directly or indirectly relate to output.
