---
title: Processing
layout: coursepage
---

Now that you've seen what a computer tries to do internally, and what kind of input it's given, how does it actually do what it needs to do?

To find out, let's look at a small example. To illustrate how something as complex as a CPU works, we'll need to make some assumptions.

- In some way, the processor is able to get input from a file, in the form of 8 (bits) independent signals.
- The processor has a timer built in, and will automatically change the inputs after the last instruction was completed.
- Addition is able to be completed using two 8 (bits) inputs, outputting 8 (bits) independent signals

As you can imagine, this is not a completely realistic model of how a real computer would work. It does, however, illustrate the concept.

You can now imagine how an instruction like this would be processed.

    var     DB 64       ; store 64 as var
    add     var, 5      ; Add 5 to var, store in var

You first see the familiar declaration of a static piece of memory, `var`. Then, addition is performed on `var` with the literal value `5`.

The CPU would do the following when adding.

1. redirect input from the `var` registry into the first byte input on the adding machine
2. form and direct input from a value of 10 (binary: 00000101) into the second byte input on the adding machine
3. redirect output from the adding machine into the memory location of `var`

In the end, `var` will contain 69 (binary: 1000101).

Let's illustrate the idea.

![](/img/CPU-add.png)

The complexity of such a simple task would indicate that creating large programs like this would be likely impossible. Imagine all of the complicated procedures that have been needed just to show you this webpage.

This is the reason for things like programming languages, libraries, environments, etc. A programmer's job would be much harder if he/she were left to sift through every single detail. Let alone making a program compatible on different computer architectures and CPUs.
