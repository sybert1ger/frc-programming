---
title: Power
layout: coursepage
---

Power is a necessary component of any control system - it is the underlying movement that makes everything we do possibly. Everything involved in controlling a system is rooted in electricity and it's utility to us.

But power is not a simple binary system. There are different kinds of electricity -  resistance, amperage, voltage, power, grounding, conductivity, etc. are all pieces of the puzzle.

### AC vs DC
One of the most popularly understood aspects of electricity is AC and DC.

Alternating Current (AC) is an electrical current that frequently reverses direction. Effectively, it changes from negative to positive current at a regular speed. This speed is measured in Hertz. Hertz is a measurement of frequency, and indicates how many times it switches in one second.

60hz means that the current is reversed 120 times in a second (because current is reversed twice in a cycle).

Why do we use AC instead of it's much simpler to understand cousin, DC? A few reasons:

- **Cost** - this is a big one. AC is easier to generate, better at going to high voltages, and the equipment that makes and uses it is cheaper.
- **Distance** - AC power travels longer distances compared to DC.

Simply put, AC is more efficient.

Direct Current (DC) is an electrical current that is generally consistent in voltage. It is much more straightforward, and the only measurement that would change in comparison to AC is the voltage. (AC is still measured in volts, but refers to the maximum points of the wave - DC refers to the actual voltage that is being outputted) DC can have negative voltage, but AC can't.

### Grounding
The term "ground" can mean different things. When a circuit is looked at locally, ground is simply the one net someone picked to call 0V so that all other voltages are understood to be relative to it. Voltage is after all a relative concept. There is no such thing as 20V absolute, only 20V here with respect to there. "Ground" is a handy short form for a common there so you don't have to keep saying it.

If a ground is not actually attached to the earth, we refer to that as "floating".

Such a ground is often chosen to be the negative supply voltage. That makes other voltages positive, which just makes things mentally easier. In general you try to chose ground as the point in the circuit signals and the like are referenced to by individual subsections. Usually there is a clear and obvious choice. Sometimes you just have to pick one.

The other "ground" refers to real earth potential, or at least the potential of the general surroundings. This matters when power and signals are coming from or going outside your little circuit. For power and safety, you have to assume a user could be tied to this ground, and you have to make sure you don't have a dangerous potential to ground to avoid zapping someone. Earth ground can also matter for radio systems since some types of antennas actually use the earth as part of the overall antenna system.
