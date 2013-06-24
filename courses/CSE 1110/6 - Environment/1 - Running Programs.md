---
title: Running Programs
layout: coursepage
---

So now that you've written some programs, how exactly does the process of running them work?

# Compilers
Compilers create executable files. There are differing ways to do this, but they all accomplish that same basic goal. Some create files that an operating system can run, and some create files that run on a *virtual machine*. This means that there is a program that runs the actual program on top of it, keeping track of resources and memory usage. This has an added benefit of being platform-independent; the program can be run on any computer or device with the virtual machine installed.

#### Programming Languages that use compilers:

- C
- C++
- C#
- Objective C
- Haskell
- Fortran

Most of these are low-level (less libraries in place).

### gcc
One of the most used compilers of all time, gcc is the fundamental ground of development in the C programming language. Even many programming languages are themselves written in C, including Java, Python and others. GCC compiles programs into Operating System executable files.

### Clang
Clang is like the modern version of gcc. Even though gcc is still developing, it has become less "bleeding-edge" and more of a stable ground. Clang is used most famously for the Objective C (iPhone and Mac) and C++ programming languages. Clang compiles programs into Operating System executable files.

### JavaC
JavaC is the Java compiler. It compiles Java programs into something called *byte code*. The Java Virtual Machine (JVM) runs these byte code files. There are many versions of JavaC, including Oracle Java SE to OpenJDK.

# Interpreters
Interpreters runs files directly. In real time, they look at the instructions and decide what to do with them. This makes them more fragile because errors can creep up during runtime, but also more flexible, letting the programmer have less unnecessary code.

### Python 
CPython is the default python bytecode interpreter. It compiles and runs python files. The interpreter automatically frees and uses memory as needed by the program, since it is a virtual machine.

### JVM
Arguably the most used virtual machine ever, the Java Virtual Machine is not only used for Java code. Even python code can run on the JVM!

![](http://upload.wikimedia.org/wikipedia/commons/3/3a/Java_virtual_machine_architecture.svg)

List of languages that can be compiled and run on JVM

<iframe src="http://en.wikipedia.org/wiki/List_of_JVM_languages" style="width: 80%; height: 900px"></iframe>

A virtual machine is an application that is written and compiled for multiple platforms. It runs programs written in a specific programming language or bytecode.
