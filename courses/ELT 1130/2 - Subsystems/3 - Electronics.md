---
title: Electronics
layout: coursepage
---

The electronics subsystem can become very complex, or very simple. It will depend on the actual functionality and elements that are used in the design.

![](/img/electronics.png)

This diagram represents a basic overview of most robotic electronic systems. Most of the control revolves around the processor, which makes the decisions of what output should be given.

### Signal Dispatcher
The signal dispatcher is any electronic component that takes output from a processor and transfers the data into direct signals for outputs.

### Controllers
The controllers are devices that take input from a signal dispatcher and transfer that into somethings that actuators use. For example, motor controllers adjust the voltage going to a motor based on the signal it receives.

### Signal Receiver
Most processors cannot directly interpret signals from input. A signal receiver is some kind of device that processes the input into a readable format for the processor. This is usually done because signals are not safe enough to be given directly to the processor.
