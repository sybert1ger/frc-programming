---
title: Loops
layout: coursepage
---

There are two different kinds of loops used in control systems - software and hardware. We'll explore both of them.

# Hardware
In hardware, a loop is a circuit that gives itself input. We'll look at one of the most used loops of all time - the flip-flop.

Imagine you need to save a value somewhere for later usage. You need to be able to change that value too. Well, you need to formulate a circuit like this:

<div class="credited">
<p><a href="http://commons.wikimedia.org/wiki/File:R-S_mk2.gif#mediaviewer/File:R-S_mk2.gif"><img src="http://upload.wikimedia.org/wikipedia/commons/c/c6/R-S_mk2.gif" alt="R-S mk2.gif"></a><br>"<a href="http://commons.wikimedia.org/wiki/File:R-S_mk2.gif#mediaviewer/File:R-S_mk2.gif">R-S mk2</a>" by <a href="//commons.wikimedia.org/wiki/User:Napalm_Llama" title="User:Napalm Llama">Napalm Llama</a> - Modification of Wikimedia Commons file R-S.gif (shown below). Licensed under <a href="http://creativecommons.org/licenses/by/2.0
" title="Creative Commons Attribution 2.0
">CC BY 2.0</a> via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.</p>
</div>

This might look confusing at first. `R` is the "reset" signal. It turns Q off. `S` is the "set" signal. It turns Q on. Q with a line on top means "not Q".

Turning on S turns off the NOR gate, and provided that R is off, subsequently turns on the R NOR gate. This turns on Q and turns off NOT Q. So, in practicality, S turns on Q and turns off NOT Q. R does the same thing, but reversed (Q = OFF, NOT Q = ON).

Turning on both R and S turns both Q and NOT Q off. This is known as an "invalid" case because it does not follow the definition of NOT Q. Q and NOT Q cannot be equal.

There are different kinds of flip-flop loops as well. The most notable is the gated SR latch.

<div class="credited">
<p><a href="http://commons.wikimedia.org/wiki/File:SR_(Clocked)_Flip-flop_Diagram.svg#mediaviewer/File:SR_(Clocked)_Flip-flop_Diagram.svg"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/SR_%28Clocked%29_Flip-flop_Diagram.svg/1200px-SR_%28Clocked%29_Flip-flop_Diagram.svg.png" alt="SR (Clocked) Flip-flop Diagram.svg"></a><br>"<a href="http://commons.wikimedia.org/wiki/File:SR_(Clocked)_Flip-flop_Diagram.svg#mediaviewer/File:SR_(Clocked)_Flip-flop_Diagram.svg">SR (Clocked) Flip-flop Diagram</a>" by <a href="//commons.wikimedia.org/wiki/User:Inductiveload" title="User:Inductiveload">Inductiveload</a> - Own Drawing in Inkscape 0.43. Licensed under Public domain via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.</p>
</div>

E is a signal that tells the flip flop that it can be set. If E is not on, R and Q do nothing.

One last important concept is a *rising-edge* flip-flop. This means that, for example, in the gated SR latch, turning on E will only save values for the instance it has turned on. Afterwards, it is not capable of changing, even with E on. Rising edges require somewhat more complex circuitry, although it isn't unreasonable.

A complete guide of the different types of flip flops can be found [here](http://www.ee.usyd.edu.au/tutorials/digital_tutorial/part3/fl-types.htm).

Remember, flip flops are not the only electrical circuit that use loops. The key concept here is that an output is used as an input.

# Software
Software uses loops in a different way. Loops are done using *jumping* or *branching*. Imagine a simple program:

    1: X = 12
    2: ADD 13 and X
    3: MULTIPLY X and 2

If you wanted to do this 3 times, you'd do something like this:

    1: INDEX = 0
    2: X = 12
    3: ADD 13 to X
    4: MULTIPLY 2 to X
    4: ADD 1 to INDEX
    5: IF INDEX < 3: JUMPTO 3

This would execute the instructions 3 times. Index gets incremented by one three times until INDEX >= 3.

Loops in software are much closer to electronics than you'd imagine. What's really going on is ~8 latches (sometimes even flip-flops!) are addressing a section of the code to run, and it increments by one each time. A `JUMPTO` instruction will change the address to the line.
