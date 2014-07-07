---
title: Control
layout: coursepage
---

A control system is a device that controls the behaviour of other devices or systems. The key concept that control systems use is *control*. This can refer to multiple things.

- User input - When the control is through some kind of user controlled input.
- Hardware - When the control is through some kind of hardware. Most of the time this is something like a sensor.
- Software - When the control system is controlled by some predefined functions with inputs and output.

It can be one or a combination of these forms of control. Let's look at a few different kinds of control that use our relays and loops.

## Computers
Although computers obscure the definition of what exactly a control system is, they are still classified as one. This is because there is a device whose behaviour is determined by input.

There are multiple computer components that use sophisticated control systems. One of which is the processor. A processor is the combination of adding circuitry, registries and caches. Modern processors include very sophisticated circuitry that can perform actions in memory very quickly.

You might be surprised that an entire processor with memory can be constructed using simple relays. Of course, this would be impractical. But it is certainly theoretically possible. Specifically, a simple 8-bit (binary number with length of 8) adder looks like this:

![](/img/8-bit-adder.png)

The `FA` looks like this:

![](/img/full-adder.png)

`Cin` and `Cout` are carries. This is similar to "carrying the one" in decimal numbers.

This control system is capable of controlling the output of a display of a calculator. All you need to do is enter two values. These kinds of controls are more often used for more complex tasks, however. They are often only part of a control system.

## Mechanical Control
Unlike computers, mechanical devices make control systems affect physical space in an important way. Mechanical devices all need to be controlled as well.

Mechanical devices can use two techniques, or a hybrid, for control.

- Direct control - Input from the user is directly outputted to the device. This is usually used in less complex and/or dangerous devices.
- Computer control - Input is predifined far ahead of time, and is executed by a computer. Often, extra input affects the output of the device. This allows for safety measures and more accurate control.

These are subsections of the first three controls on this page.

Some examples of mechanical control are microwaves, CNC milling machines, 3D printing machines and robots. All of these use different combinations of input to perform their function.
