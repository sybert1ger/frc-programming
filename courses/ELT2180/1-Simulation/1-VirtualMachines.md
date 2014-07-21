---
title: Virtual Machines
layout: coursepage
---

Virtual machines are very good examples of how simulation works. They demonstrate the key qualities of a simulation:

- Emulates or resembles something else, without the elements of that system
- Is practically indistinguishable from the thing it is resembling
- Can be used to understand the original system

Of course, it is impossible for these three qualities to be completely accomplished. There are *degrees* of simulation. For example, you might want to simulate cold climates in a small room. There could be different degrees of simulation to do that.

1. Air conditioning to make air colder
2. Added humidity to make ice form
3. Artificial snow
4. Artificial wind and snow
5. Added arctic animals and small lake

As you can tell, #1 is very different from #5. The extent of a simulation is extremely important to take note of.

### Computer simulations
Simulations in computers would be different than most real-life simulations. There is a higher bar set to be considered a simulation of a computer. And there are further kinds of simulations,

- Computers simulating other computers (different architectures, software, hardware, etc.)
- Computers simulating real life (training exercises, video games, etc.)
- Real life simulating computers (smaller scale computers, less advanced hardware, etc.)

\#2 is the most common use of this, followed by #1. #3 is less common, because it there isn't much of a practical use for it, other than learning purposes.

### Virtual Machines
Computers simulating other computers - why do we do this? Well, usually we have an ulterior motive - something specific to learn about the computer we are simulating. Or, we might actually want more than one computer, but are limited by money or space. We can simulate having those computers using virtual machines.

There are a variety of ways that virtual machines are implemented. We will focus on the "simulation of computers" elements of virtual machines. Other ways exist, like the Java Virtual Machine, a piece of software that emulates a standard set of ways to interact with any kind of computer. The big difference is that "simulations of computers" focus on an entire operating system running, instead of one single application.

[VMWare](http://www.vmware.com/ca/en/), [VirtualBox](https://www.virtualbox.org/), etc. all provide a virtual machine to run operating systems on. They emulate the x86 architecture of computers, allowing the user to run virtually any modern operating system on them.

![](http://thesystemmaster.com/images/vm_w7_under_xp.jpg)
