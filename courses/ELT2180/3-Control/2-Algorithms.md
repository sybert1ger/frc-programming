---
title: Algorithms
layout: coursepage
---

Algorithms are the fundamental building block of software. They are the control sequences used in the processor to find a desired output to the system. Typically, algorithms are relatively simple. For example, this is what an "arcade drive" algorithm looks like:

<script src="https://gist.github.com/joelg236/a294a03a1094167ff49f.js" type="text/javascript"></script>

Obviously we don't expect you to understand the syntax here exactly, but you should get the general gist of what an algorithm does. Most algorithms **take an input** and **return some kind of output**. In this case, the algorithm takes three inputs, and returns output to the system in terms of left and right output (speed from [-1 to +1]).

We can relate this back to parameters - **moveValue**, **rotateValue** and **squaredInputs** are all parameters.

- Move Value is a decimal value from [-1 to +1]
- Rotate Value is a decimal value from [-1 to +1]
- Squared Inputs is a boolean value that is either on or off
