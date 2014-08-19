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

<div class="credited">
<p><a href="http://commons.wikimedia.org/wiki/File:H_bridge.svg#mediaviewer/File:H_bridge.svg"><img src="http://upload.wikimedia.org/wikipedia/commons/d/d4/H_bridge.svg" alt="H bridge.svg" height="283" width="461"></a><br>"<a href="http://commons.wikimedia.org/wiki/File:H_bridge.svg#mediaviewer/File:H_bridge.svg">H bridge</a>" by Cyril BUTTAY - <span class="int-own-work">Own work</span>. Licensed under <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a> via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.</p>
</div>

There are two directions for the voltage to flow, one forwards and one backwards.

### DAC
A simple Digital-to-Analog Converter is also an option to control voltage. By converting a digital value (your output) to an analog voltage, you can power simple circuits. Usually, DACs cannot handle large currents, so they are usually useful for smaller circuits without any significant load.
