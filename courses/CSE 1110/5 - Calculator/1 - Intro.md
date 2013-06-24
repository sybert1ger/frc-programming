---
title: Intro to Calculator Activity
layout: coursepage
---

You'll be making a basic text-based single-operation calculator. There are a few things you'll need to know in order to do this.

- Remember that `raw_input()` and `print(x)` are for input and output
- Remember that `if - elif - else` statements are useful to categorise input
- Use the `in` keyword to check if one string is found within another
- Use `float(x)` to convert a string to a float

To help you out, here is a function that will give you the numbers around the symbol - don't worry about exactly how it works:

    def firstNu(fullLine, symbo():
        return fullLine[0:fullLine.find(symbol)].strip()
      
    def secondNumber(fullLine, symbol):
        return fullLine[fullLine.find(symbol) + len(symbol) : len(fullLine)].strip()

Remember that google is your friend. Put "python" inside of your searches.
