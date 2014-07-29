---
title: Tuning
layout: coursepage
---

Oftentimes, when dealing with a system, you have an ideal "output" that you want to see. Usually, this is a position, speed or state. To achieve this ideal, you might not have a perfectly accurate system. For example, you might have a robotic arm that you want to go to a specific angle. But the motor that moves the arm is not a stepper motor and has inaccuracies.

So, how do you go about **tuning** this system? You might start with increasing and decreasing the speed of the motor in the feedback loop. Then, you might add resistance to the joint to slow the movement down. You might even try to add a second sensor that measures the angle in a different way.

These are examples of basic tuning. You might think of tuning as adjusting elements that already exist, but it's entirely possible to add new elements as part of your tuning. Adding new sensors is an especially useful way to tune systems - oftentimes having redundancy makes it possible to achieve better results.

Tuning can be done in software and hardware. In software, you will often be adjusting coefficients or algorithms to make the system more dynamic or better adjusted for the environment. In hardware, you will usually try to eliminate variables and environment factors that change your result.

Slowing things down is a common method of tuning. There is a balance to be struck between a slow system and an accurate one. You don't want it to be too slow, or too inaccurate. Slowing down works because there is more time for the system to adjust itself, without having to overshoot and other related problems.

![](http://www.mathworks.com/matlabcentral/fileexchange/screenshots/2116/original.jpg)
