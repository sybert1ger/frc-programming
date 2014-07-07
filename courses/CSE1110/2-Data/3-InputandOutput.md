---
title: Input and Output
layout: coursepage
---

An important part of computer programming is being able to interact with the user. This includes telling them things, and taking input from them.

Remember that all input and output in a console is done through strings. Every input or output is a string value.

In python, input and output are very easy.

# Input
To get the input from the last line in the console, use `raw_input()`. This is always a string. You can call `eval(raw_input())` to convert it to a number.

# Output
To print to the console, use `print(output)` and replace `output` with your output.

# Example

    print("What's your name?")
    name = raw_input()
    print("What's your age?")
    age = int(raw_input())
    print("What's your gender?")
    gender = raw_input()

    print("Hello, " + name + ". You are " + str(age) + " and a " + gender + ".")

Remember that `age` is actually a number, so to print it, it needs to be converted into a string using `str(age)`.

Try and make sure you understand everything going on here.
