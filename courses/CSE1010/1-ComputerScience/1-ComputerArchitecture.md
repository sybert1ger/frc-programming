---
title: Computer Architecture
layout: coursepage
---

Computers are a very recent invention, and have proven to be one of the most influential creation of all time.

This course will begin to explain what computers are, what they do and how they do it. You'll begin to grasp how to make them do what you want.

The real power of a computer is its flexibility. This differentiates computers from other pieces of technology. Instead of having one purpose and only being capable of fulfilling that purpose, computers are machines capable of taking instructions on what to do (and sometimes how to do it).

At the base of this power, however, computers are simple machines.

## Processors
Unlike brains and other high-level processing units, computer processors (known as CPUs) work at the lowest level possible. Every single action required from your computer involves one of these few things:


- Arithmetic (usually addition, but multiplication, division and subtraction are usually possible)
- Boolean logic (check if two things are the same, different, etc.)
- Memory capabilities (move to another section in the code, transfer memory from one spot to another, etc.)
- Timing ("cycles" can regulate certain actions)

## Architecture
Computer architecture describes how a computer system works by it's physical components and their relations to each other. Most of computer architecture is focused around how the CPU (Central Processing Unit) functions.

For the most part, the CPU can be described as an "in-out" machine. Simply put, it takes input from some sort of memory or register, and takes some kind of action based on that input. The exact ways in which this machine works is much higher level than this course will describe, however we can examine the effective differences between architectures.

#### x86
x86 is the defacto standard for most modern processors. In reality, x86 doesn't really describe the physical unit. It describes what kind of input you can give it.

But this tells us a lot about the architecture of a CPU. Look at an example of assembly on x86:

    var      DB 64      ; Declare a byte containing the value 64. Label the
                        ; memory location “var”.
    var2     DB ?       ; Declare an uninitialized byte labeled “var2”.
             DB 10      ; Declare an unlabeled byte initialized to 10. This
                        ; byte will reside at the memory address var2+1.
    X        DW ?       ; Declare an uninitialized two-byte word labeled “X”.
    Y        DD 3000    ; Declare 32 bits of memory starting at address “Y”
                        ; initialized to contain 3000.
    Z        DD 1,2,3   ; Declare three 4-byte words of memory starting at
                        ; address “Z”, and initialized to 1, 2, and 3,
                        ; respectively. E.g. 3 will be stored at address Z+8. 

You don't really need to understand exactly how this works or what it does, but it should give you an idea as to how the input will look to a computer.

For more information on x86 assembly, see [a tiny guide to programming in 32-bit x86 assembly language](http://www.cs.dartmouth.edu/~sergey/cs108/tiny-guide-to-x86-assembly.pdf).

To a computer, something like this

    var      DB 64

will be everything it needs to know about the current instruction to perform. As you can imagine, the words that appear after semi-colons in the above example are ignored by the computer. They are known as "comments", things meant solely to help humans read the instructions.

Let's looks a little more closely at what something like the var instruction really does.

    var
    
this tells the computer that the memory location is known as "var". The functionality of this would be different for different processors. Something like an [Intel 8086](http://en.wikipedia.org/wiki/Intel_8086) would likely simply find the next piece of available section of memory. A modern processor might have more advanced techniques like caching and piping.

    DB

Standing for Declare Byte, this declares a static data region. By convention, this is basically declaring some kind of usable variable to be used later in the program.

    64
    
This indicates that you wish the byte (4 bits, binary data) as the value of 64.

# Instructions
We don't want to dive too deeply into the core of Assembly language too quickly (phew!), but before we move on you should get a feel for the kinds of instructions that a computer can handle, using x86 as an example.

    mov <reg>,<reg>     ; Moves memory from one region to another
    push <reg>          ; Pushes the memory onto the top of the stack in memory (basically, a list of values)
    pop <reg>           ; Pops the memory from the top of the stack in memory into the registry given
    add <reg>,<reg>     ; Adds two values storing the result in the first operand
    sub <reg>,<reg>     ; Same as add, but subtracts the second value from the first
    inc <reg>           ; Adds one to the value

These are only some example, and as you can imagine the list of possible functions is quite expansive.
