---
title: Control Loop Logic
layout: coursepage
---

We have a simple circuit, with 3 elements.

- Battery
- On / Off switch
- Motor (fan attached)

We want the switch to change the on/off state of the motor. You can probably easily imagine that circuit.

![](/img/basic-motor.png)

But, you find out that this motor will become dangerous after operating for a few minutes. You want to have some kind of safety mechanism in the circuit, to prevent danger.

For the sake of understanding, we will assume that when the motor becomes dangerous it hits a "limit switch" - in this case indicated by the red button.

![](/img/safety-switch.png)

When the red button is hit, the motor is turned off.

![](/img/safety-switch-on.png)

We could accomplish the same goal with a flip-flop switch. Except in this case, the on/off switch is only a button (as flip-flops require)

![](/img/safety-flipflop.png)

This kind of basic logical circuit is used in many applications. It is useful because there are no potential "bugs", as there would be with software. You know for sure that the circuit will be cut off when the safety is hit.

A more advanced control loop could be implemented as a pure electrical circuit. Even something such as PID could be - although the math required for that would likely require a relatively complex circuit board.

Example:

[![](http://www.ospid.com/blog/wp-content/uploads/2011/12/osPIDKitNaked.jpg)](http://www.ospid.com/blog/resources/hardware/)
