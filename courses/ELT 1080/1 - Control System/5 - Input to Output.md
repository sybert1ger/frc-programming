---
title: Input to Output
layout: coursepage
---

Something very important to control theory that we haven't discussed is how input affects output. We know that it does, but how would it be accomplished? Let's look at two prominent examples in industry. Both can be implemented in software or in direct circuits in hardware. They both run in loops, adjusting every time the loop runs.

## PID Control
You may have even heard of PID before ever understanding control theory. PID is a method of output control that is used for systems with multi-direction positional or velocity systems. It comes down to having a "setpoint" - somewhere that we want the input to be.

PID has one input (we'll call it `In`) and one output (`O`). We want `I` to match `O` as closely as possible.

PID's main attraction as a form of control is it's ability to compensate for difference. PID stands for Proportional, Integral and Differential. Don't be intimedated however, as these are pretty basic. The output will simply be a sum of these three components.

    PID = P + I + D

So let's look at each component individually.

    P = Setpoint - In

Proportial is basically how far away we are from the setpoint. This lets output get smaller as we approach the setpoint.

I is the most complicated section here. Basically, it accumulates past errors, and slowly gets higher if input doesn't change fast enough. It is useful if stalls are an issue.

    D = Error - PreviousError

Differential accounts for changes in error. Error is just how far the input is from the setpoint. D is used mostly to slow down the approach to the setpoint, along with P.

Adjusting the behaviour of PID is as simple as changing 3 coefficients for the three terms. I opperates slight differently (it is divided by cI).

PID is used in many industrial uses, especially in movement applications where a constant signal is needed.

## Bang-Bang Control
If you aren't in need of bi-directional control, bang-bang control is very useful. It is especially good because of its simplicity.

Imagine you need to heat a room to 20 degrees. You're approach is most likely this.

    Turn on heat when temperature is less than 20.

This is exactly what bang-bang does. When the input is less than the setpoint, it is set to 100%. There is only on and off.

You can make variations on bang-bang if needed, but the general idea is to keep it simple. Anything without the capacity to "overshoot" a goal is ideal for bang-bang because the input will settle down at the setpoint without trouble.
