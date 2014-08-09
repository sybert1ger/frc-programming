---
title: Calculator
layout: coursepage
---

Here's is a calculator program that takes input from the user, and evaluates that result.

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


Try it [here](http://repl.it/WPk), press "run session".
