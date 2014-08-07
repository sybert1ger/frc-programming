---
title: Virtual Machine, Machine Code and Efficiency
layout: coursepage
---

We've talked about performance of languages, and noted that virtual machines and byte code have an effect on the efficiency of software (notably in Java).

Why?

A **virtual machine**, such as the [JVM](http://en.wikipedia.org/wiki/Java_virtual_machine) (Java Virtual Machine) is a piece of software that runs **byte code**. Byte code is a lower-level compiled file that contains instructions for the virtual machine to execute. You can think of this an a completely different language than Java, but higher level than machine code.

The defining quality of byte code is that it is executable on any platform, CPU, memory, etc. Machine code is specific to a computer - it's been compiled with a specific platform in mind and has instructions that will likely only able to be run on one kind of computer.

Byte code, on the other hand, can be run anywhere with a JVM. The biggest advantage of this is operating systems - you don't need to do anything differently to run a Java program in Mac compared to Windows or Linux.

This all comes at a cost though - the JVM needs to be capable of doing any instruction that byte code gives it. And it's up to the JVM to be efficient at doing it.

Virtual machines need to be developed for every environment that it's run on. So, the Mac JVM could be more efficient at running copying instructions compared to the Windows JVM. The functions are standardized, but the performance is far from standardized.

You, as a "byte code developer", rely on the virtual machine to be well written. And this is rarely a guarantee.

It's certainly a tradeoff to write code that runs on a virtual machine. And frankly, we wouldn't even consider this an option if Java was not a well used and popular option for FRC programming. It just doesn't make sense to do, unless it's done *very* well.

For more information on running programs, see [this](/courses/CSE1110/6-Environment/1-RunningPrograms/) page.
