---
title: PID Control
layout: coursepage
---

PID is one of the most discussed and used closed-loop controllers in all of robotics. It is the common way to "get to a desired output". Typical use cases are:

- Keeping a movable object in one position
- Moving an object to a different, set position
- Dynamically keeping speed at a consistent rate

Generally, you will have two use cases:

1. Keep input where it is
2. Move input to a set position

Because there are so many use cases, we have to use vague language. Let's look at an example to get a better feel for what we're talking about.

### Example
We have a robotic arm that looks like this

<div class="credited">
<a href="http://commons.wikimedia.org/wiki/File:Robot_arm_model_1.png#mediaviewer/File:Robot_arm_model_1.png"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Robot_arm_model_1.png/1200px-Robot_arm_model_1.png" alt="Robot arm model 1.png"></a><br>"<a href="http://commons.wikimedia.org/wiki/File:Robot_arm_model_1.png#mediaviewer/File:Robot_arm_model_1.png">Robot arm model 1</a>" by <a href="//commons.wikimedia.org/wiki/User:NeD80" title="User:NeD80">NeD80</a> - Этот файл был создан с использованием Autodesk 3ds Max 2009 64-bit. Licensed under Public domain via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.</p>
</div>

Let's ignore the fact that it has two axises - we only care about the first joint, up and down.

But we have various positions for this joint, which we want the arm to go to at the press of a button.

- Up = sensor feedback of 0
- Middle = sensor feedback of 2.5
- Down = sensor feedback of 5

So to think of PID, let's first imagine it being a black box. You don't know what's inside, and you don't care. All you care about is that it works.

Your code to go to the positions looks like this (pseudocode):

    if (button1 is pressed)
        gotoposition(UP)
    if (button2 is pressed)
        gotopositioin(MIDDLE)
    if (button3 is pressed)
        gotopositioin(TOP)

Makes sense. But what is happening internally on the PID?

PID = P + I + D

P is proportional. It is literally how far away you are from your setpoint.

I is integral. It is the sum of all P values, and acculumates over time.

D is derivative. It is the "slope" or the change in P from the last loop.

There are three constant coefficients that are multiplied against P I and D. These coefficients affect how much you want the different terms to add to the final output.

You would want more P if your error is very small compared to the needed output. Too much P will cause overshoot, resulting in your input never finding the setpoint.

You would want more I if your input gets very close to the desired setpoint, but not close enough with the current P value. This will slowly bring the input closer to your setpoint. Too much I will result in huge swings - it should not be even close to the P value.

You would want more D if you need faster swings towards the setpoint. Basically, D is a "jumpstart" to your correction, it adds some push in the initial and middle stages. Too much D will also cause overshoot.

Basic PID code would look like this:

    P = 1
    I = 1
    D = 1
    
    i = 0
    lastError = 0
    
    setpoint = 2.5
    
    while (true) {
        p = setpoint - input()
        i += p
        d = p - lastError
        lastError = p
        
        setOutput(P * p + I * i + D * d)
    }
    
For a more complete example, see [this](https://github.com/Team4334/atalibj/blob/master/src/edu/first/module/controllers/PIDController.java) implementation.
