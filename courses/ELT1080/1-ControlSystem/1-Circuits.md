---
title: Circuits
layout: coursepage
---

At the heart of a control system is circuits. You can't have an electrical system without somehow moving electricity around it. Let's explore some simple control circuits that allow systems to be controlled.

First, this is a switch.

![](/img/switch.png)

Switches are a basic component, but can give the user control over anything. Think of a switch like a light switch. You have an on and off position. On lets electricity move through it, and off does not.

Imagine you want to communicate with your friend using electricity. Maybe his house is a few doors down. How would you do it? Well, your first option is to use a circuit that goes from his house to yours. But how would you talk to him?

You investigate a bit, and learn about morse code. Simple combinations of short and long signals can be turned into letters, and then words.

<div class="credited">
<p><a href="http://commons.wikimedia.org/wiki/File:International_Morse_Code.svg#mediaviewer/File:International_Morse_Code.svg"><img src="http://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg" alt="International Morse Code.svg" height="480" width="372"></a><br>"<a href="http://commons.wikimedia.org/wiki/File:International_Morse_Code.svg#mediaviewer/File:International_Morse_Code.svg">International Morse Code</a>" by Rhey T. Snodgrass &amp; Victor F. Camp, 1922 - <a href="//commons.wikimedia.org/wiki/File:Intcode.png" title="File:Intcode.png">Image:Intcode.png</a> and <a href="//commons.wikimedia.org/wiki/File:International_Morse_Code.PNG" title="File:International Morse Code.PNG">Image:International Morse Code.PNG</a>. Licensed under Public domain via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.</p>
</div>

So at least you now have a circuit, and a code. But after wiring a long wire from his house to yours, you find out that the voltage of a battery cannot go far enough. You both have switches at each end, but the electricity doesn't have enough strength to go around the entire loop. You imagine a device that "boosts" the signal.

This device is known as a relay.

![](/img/relay.png)

You can see that this device affects a switch. The black bar is a metal rod. Remember that sending a current through loops around a metal will induct a magnetic force. When a current is sent through the bottom wires, the metal rod becomes magnetic and pulls the switch down. This makes a "clunk" type sound.

But how does this help us? Well, if you hook up your input signal to the bottom wires and hook up the output to the top wires, you boost your signal. A current that runs through the electromagnet causes the current to flow through the top portion. You can add a second battery to that top portion.

![](/img/relay-with-friend.png)

Now you have four batteries. You've effectively doubled the potential distance that the signal can travel.

You can imagine how you could use multiple relays in a row to extend a signal.

![](/img/relay-extending.png)

So now we have a 2-way communication device that can (theoretically) extend for an infinite distance given enough batteries and relays.

## Gates
Something you might wonder is if these devices are useful for other applications. And the answer is yes. Actually, with wires and relays, you can actually construct a full computer. Obviously this is not a simple task, and mechanical relays are large and slow. In reality, computers are made out of transistors, which are very small and fast. But at the most basic understanding, they operate in the same way as a relay.

In control theory, we use things called gates. These are small basic pieces of circuits that create logical effects. Let's explore some of these gates.

#### AND Gate
The first gate that we'll explore is an AND gate. This gate takes two signals, and outputs one signal based on if *both* signals were on.

This is a pretty basic concept after seeing it.

![](/img/and-gate-circuit.png)

The two IN signals need to be on for the circuit to finish.

In electronic diagrams, this will be simplified to this symbol:

![](/img/and-gate.png)

#### OR Gate
Sometimes you only want to know if one of the signals is on. We use an OR gate for this.

![](/img/or-gate-circuit.png)

In electronic diagrams, this will be simplified to this symbol:

![](/img/or-gate.png)

#### NOT Gate
By far the simplest (and in some ways most useful) gate is the NOT gate. This simply reverses the signal. Remember how in a relay, the switch defaults to the top output? If you apply that output signal, it is always the opposite of the input of the relay. So, the NOT gate is only one relay.

![](/img/not-gate-circuit.png)

Not gates are shown like this:

![](/img/not-gate.png)

You can attach a not gate after any other gate. To shorten this, use a small dot in front of the symbol. For example, an NOT AND (NAND) gate.

![](/img/nand-gate.png)

#### XOR Gate
Similar to an OR gate, XOR gates only output if only one of the two inputs is on.

![](/img/xor-gate-circuit.png)

In electronic diagrams, this symbol will be used:

![](/img/xor-gate.png)

There are many other different gates, but these are the simplest and most useful. You can make some powerful circuitry with just these three gates.
