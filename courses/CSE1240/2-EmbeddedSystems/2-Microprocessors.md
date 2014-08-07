---
title: Microprocessors
layout: coursepage
---

Embedded systems are typically powered by **microprocessors** - small integrated circuits that are capable of executing given instructions.

Typically, when talking about embedded systems, and specifically robots, processors are known as the "brain" of the control system. It is where inputs are processed, and outputs are given. The entire system relies on the processor to make decisions on what to do next, otherwise very little will happen.

In FRC, the compact RIO has traditionally been the processor. In 2014 and onwards, the [roboRIO](https://decibel.ni.com/content/docs/DOC-30419) will replace it.

![](/img/roboRIO.png)

It is a highly integrated machine - all inputs and outputs are basically integrated directly onto the board. In previous years, the DIO, PWM Control, I^2C, relay, analog input, etc. were all on breakouts from the main microprocessor. As you can tell, having all of these on one board makes things easier.

But there is a disadvantage to this design. When all components are on one board only, any electrical problem could spell disaster. Instead on only having to replace one breakout board, you might need to replace the entire processor - a much more expensive endeavour.
