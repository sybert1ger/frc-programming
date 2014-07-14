---
title: Control Systems
layout: coursepage
---

The control system is a combination of devices, sensors, processors, etc. It encompasses everything that "controls" the actual system, in this case a robot.

To simplify things, we'll think about the FRC control system.

![](/img/frc-control-system.jpg)

We won't worry about the specifics, especially considering this layout is outdated as of 2014. We will instead talk about how there are many elements that work together to accomplish a goal.

Mainly, we have a power source, devices operated from that power, and regulating devices that change the operation of the actuating devices.

Power sources are things like batteries, generators and external power supplies. These provide two kinds of power, which to the power source are indifferent. One is control power, or baseline power - this is just the minimum power needed to keep the system "alive". The other is operational power - this provides the power needed to move motors, servos, solenoids, etc.

Actuators are motors, servos, solenoids, compressors, lights, etc. They perform an action in real life, usually based off of a signal sent from the main processor.

Regulating devices are speed controllers, relays, breakout boards, etc. They take a signal from the processor and do something about it - usually controlling the flow of electricity to an actuator.

Using programming, we can control these regulating devices. To you as the programmer, forgetting about the actual mechanisms used to control the robot is dangerous. Remember at all times that you are in control of the system.
