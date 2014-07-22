---
title: Controlling Voltage
layout: coursepage
---

Processes on a robot are often voltage-based. Most actuators that would be associated with robotics are. For example:

- Motors
- Servos
- Solenoids
- Compressors

Voltage changes all of these, whether it be granular like motors (changes in voltage affect speed), or binary like solenoids (only on or off).

For this reason, controlling the voltage to actuators is an important part of process control. There are a few ways we do it.

### Relays
You might remember learning about a basic relay in [ELT1080](/courses/ELT1080/1-ControlSystem/1-Circuits/). The concept of relays is important in many areas of electronics and robotics.

To use relays as a controlling device for voltage, you can use them a few different ways.

- One-way control. You can only turn it "off" or "on" using another smaller on or off voltage.
- Two-way control. There are three states of the relay; off, forwards and backwards. Voltage can be reversed using a reversed signal.

The one-way control is self explanatory, but two-way is more interesting.

### H-Bridge
The two-way relay is typically designed as an "H-Bridge", because of its resemblance to the letter H.

![](http://www.engg.uaeu.ac.ae/departments/units/gra/presentation/nd_05_06/Final%20Pres%20ss05.06/Final%20Pres-M/Mech/MEM2-1/website&poster/Website_template/projec15.jpg)

There are two directions for the voltage to flow, one forwards and one backwards.

### DAC
A simple Digital-to-Analog Converter is also an option to control voltage. By converting a digital value (your output) to an analog voltage, you can power simple circuits. Usually, DACs cannot handle large currents, so they are usually useful for smaller circuits without any significant load.
