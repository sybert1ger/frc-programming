---
title: FRC Programming
layout: coursepage
---

Note: This page is only meant for students who plan to program in FRC.

In FRC, you will need to program your robot's functionality. You have three options for programming languages:

- Java
- C++
- Labview

Each language has pros and cons.

# Java

### Advantages
- Can be programmed on Windows, Mac and Linux.
- Forces good programming patterns such as object-orientation.
- Simpler than C++.
- No explicit memory management. You don't have to worry about handling specific memory addresses.

### Disadvantages
- Incomplete vision tracking APIs.
- No explicit memory management. (Yes, this is both an advantage and a disadvantage.)

# C++

### Advantages
- Executes and compiles much faster than LabVIEW.
- Has complete vision tracking libraries.
- Explicit memory management, so you don't ever have memory leaks if you know what you're doing.
- Most popular, so more teams are likely to be able to help you at the competition.

### Disadvantages
Syntax can be confusing for new programmers.
Requires a Windows PC to upload code.

# LabVIEW

### Advantages
- Data flow is more intuitive than object-orientation in other languages.
- Arguably easiest to teach among the three major supported languages.
- Has access to the most NI vision libraries.
- Very quick debugging tools. You can probe wires in the code while you're running it to see what the problem is very quickly.
- Garbage collection means no explicit memory management.

### Disadvantages
- It's likely you know text-based languages already, so it could be harder to learn the data flow paradigm.
- Only runs on Windows PCs.

Honestly, write your programs in the language with which you are most comfortable. If you're caught between two or more, figure out which is the best for what you're trying to do. LabVIEW is much better for vision tracking than say Java, but if you need Java's higher level features, go for that.

# Resources
Some starting resources for each:

- Java: http://wpilib.screenstepslive.com/s/3120/m/7885
- C++: http://wpilib.screenstepslive.com/s/3120/m/7913
- Labview: http://wpilib.screenstepslive.com/s/3120/m/11825
