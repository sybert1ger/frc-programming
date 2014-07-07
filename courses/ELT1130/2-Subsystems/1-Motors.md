---
title: Motors
layout: coursepage
---

Motors are devices that create motion. This page will cover electronic motors.

# Motion
Motion in a motor is created using an electrical current. Most electronic motors use the current to produce an electromagnet inside of two magnets, which rotates the axle. This current constantly reverses, giving the spinning effect. See more [here](http://www.pcbheaven.com/wikipages/How_DC_Motors_Work/).

![](http://www.pcbheaven.com/wikipages/images/howdcmotorworks_1269547145.gif)

# Controlling
There are two ways to adjust the speed and torque of a motor. One is to adjust the actual voltage. This adjusts how much power the motor has, and in effect changes the speed.

The second way to adjust speed is more accurate and has more torque, but requires more complex control. It involves turning the electricity on and off very quickly, creating the adjustment of speed. This gives the motor the same amount of power, with control over the speed. This form of control is usually done through [pulse width modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation).

See more on PWM [here](http://arduino.cc/en/Tutorial/PWM)

## Braking
Sometimes it is useful to quickly stop a motor. The way that this is done is by shorting the two ends of the motor. This reverses the polarity of the signal because the motor acts as a generator.

<iframe width="420" height="315" src="//www.youtube.com/embed/oz3-sPTc34c?rel=0" frameborder="0" allowfullscreen></iframe>
