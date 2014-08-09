---
title: Control
layout: coursepage
---

Think about the circuits we made in the first module of this course. Although they may seem irrelevant, primitive and useless, they most certainly are not. In the same way that we explore letters before words, words before sentences and sentences before paragraphs in our early years, we need to understand how the insides of a processor works before utilising it. Although its certainly possible to use these devices for many years without any understanding of how they work, you won't ever truly benefit from doing so.

We've looked at quite a few different concepts that don't neccesary directly correlate, so let's take some time to step back and examine a control system.

![](/img/control-system.png)

It's probably tempting to think of the processor as a black box. Especially considering that it, by virtue of being complex, is represented that way in many diagrams. And this is okay. As long as you do not have unrealistic expectations of a processor, it is totally okay not to worry about small details.

We represent an internal feedback loop in this diagram because its a very important part of processing. This model is actually closer than you would think to the real world feedback loop. Output is saved to memory, and can be used in calculating output (I and D in PID for example).

Also, don't be confused about output for all the actuators being one line. This is just for convenience of space. In reality, each type of actuator most like has some kind of output mechanism that is separete from the processor. For example, *breakout boards* receive all signals of a certain type (ex. digital) and breakout into many different outputs. This simplifies the processor's direct output.

Notice that the entire control system can be described as some kind of loop. Although it's certainly possible that the motor does *not* affect the sensor, most of the time it does. This creates an elegant loop. 
