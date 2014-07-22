---
title: Signals
layout: coursepage
---

Signals are how programs control a physical system. They are meant to be interpreted by a physical device, usually in the goal of achieving some kind of movement. For **more information** about specific signals, see [here](/courses/CSE1240/3-RoboticControl/1-Signals/).

In simulation, signals are the difference between a physical reality and a simulated one. Signals are sent to different things in a simulation, usually they are not even electrically generated and instead are simply digitally rerouted to another piece of software.

For example, in an FRC robot, signals are sent to speed controllers (Talons, Victors, Jaguars). These speed controllers regulate voltage to motors. The signals are sent in a low power small PWM pulse-based voltage.

In a simulation, there would be two options to replace the physical components with simulations. One would be to redirect output at the signal level. Instead of sending this signal to a piece of hardware, we could send it to some simulation software.

The other option would be to redirect the "basic" output. In other words, we would not generate a PWM signal. Instead, we would simply use the 0-100 percentage value that is sent to the PWM generator.

The idea here is to understand that **signals can be intercepted at different levels of software**. From there, the simulation can gain or lose certain traits. For example:

#### A PWM signal has more granularity than a percentage value.
2. Therefore, simulations may be more accurate with more "real world" data - PWM is closer to what will happen in real life.
3. But, PWM is less useful to look at for data purposes. It is difficult to determine the actual speed needed without sophisticated algorithms. A percentage would be easier to work with as a programmer.

Theoretically, your simulation wouldn't actually demonstrate differences in between a percentage value and a PWM signal, but the reality is different. This is mostly because there is naturally small delays and errors in a signal like PWM. This is even more prevalent if the signal is run through a physical wire - outside interference and noise can effect the signal a lot.
