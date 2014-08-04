---
title: Calculator Activity
layout: coursepage
---

Create a console calculator that takes in console input and evaluates its value. Make sure it can do addition, subtraction, multiplication and division.

Here's a start

    def firstNumber(fullLine, symbol):
        return float(fullLine[0:fullLine.find(symbol)].strip())
      
    def secondNumber(fullLine, symbol):
        return float(fullLine[fullLine.find(symbol) + len(symbol) : len(fullLine)].strip())

    def isAddition(fullLine):
        return '+' in fullLine
    def isSubtraction(fullLine):
        return '-' in fullLine
    def isDivision(fullLine):
        return '/' in fullLine
    def isMultiplication(fullLine):
        return '*' in fullLine
        
    print "Enter your equation"
    equation = raw_input()
    
    FirstNumber = None
    SecondNumber = None
    Result = None
    
    if isAddition(equation):
        FirstNumber = firstNumber(equation, '+')
        SecondNumber = secondNumber(equation, '+')
        Result = FirstNumber + SecondNumber
    elif isSubtraction(equation):
        FirstNumber = firstNumber(equation, '-')
        SecondNumber = secondNumber(equation, '-')
        Result = FirstNumber - SecondNumber
    elif isDivision(equation):
        FirstNumber = firstNumber(equation, '/')
        SecondNumber = secondNumber(equation, '/')
        Result = FirstNumber / SecondNumber
    elif isMultiplication(equation):
        FirstNumber = firstNumber(equation, '*')
        SecondNumber = secondNumber(equation, '*')
        Result = FirstNumber * SecondNumber

    print Result
