---
title: Linearity vs. Concurrency
layout: coursepage
---

Everyday, you probably use your computer to do multiple tasks at the same time. You might have 3-4 programs running at any given time, and even more background processes running. Have you ever wondered how this is possible, given your understanding of how a computer works?

There are multiple physical and virtual methods to accomplish this goal. Because concurrency is such an important usage of computers, there is a high amount of pressure on manufacturers to accomplish efficient solutions.

How does it work? Let's look at two main ways of accomplishing the concurrent goal.

## Linear Threading
*Threads* are 'processes' that are run at the same time, managed by your operating system's kernel. They go through different instructions and processing, while seemingly existing together happily.

As you can imagine, most CPUs only run one instruction at a time. So how do two programs run at once? This is a concept known as prioritizing and timing.

In reality, they do not run at the same time. Their execution is constantly being managed by the kernel. To easily imagine what this looks like, imagine a lineup for grocery store cashier. Two (or more) different people are constantly checking out, and going back to the line up to buy more from the cashier.

## Concurrency and multi-core
Modern processors are equipped with multi-core processors. This means that they truly do execute two (or more) things at once.

This is a huge advantage for programs that naturally do multiple things at once. It also allows for prioritization of processes (eg. if you want one program to run faster, reserve a core for it)

There is a challenge for concurrent programming though. These separate executions often want to access and change the same variables and pieces of memory. When two threads try to change the same thing at the same time, you might end up with unexpected behaviour. In extreme cases, you could end up with corrupt memory because half of the result from one program was combined with that of another. [Race conditions](http://en.wikipedia.org/wiki/Race_condition) are common to occur when programs work on the same data.
