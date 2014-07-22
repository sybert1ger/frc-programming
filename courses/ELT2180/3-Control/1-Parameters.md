---
title: Parameters
layout: coursepage
---

When controlling processes, you need to provide **parameters** - the input that will be used as actual movement or change in the physical system. A parameter defines what you want the system to do, it is a measurable piece of information to use in the control of the system.

Something as simple as a joystick can be used as a parameter. Its axises and buttons are the input - they provide the information needed by the system to create output.

A parameter can be virtually anything - it is solely defined by what kind of input is required. This can be very broad, or very specific. In software, it is usually ideal to be broad - it allows more flexibility for the end user.

Some examples of a type of input:

- Number (eg. decimal, whole number)
- Boolean value (on or off)
- State (eg. forwards, reverse, off, etc.)
- A type of device (eg. joystick, potentiometer)

In software, you define your input as anything you want to. As long as this input can somehow affect the output of the system, it is valid. Mostly, however, you will stick to one of the four examples above.

Let's look at some examples of parameters.

##### PWM speed controller

    setSpeed 0.5
    
This sets the PWM signal to turn on half of the time. The parameter is a decimal number between -1 and +1. (Number)

##### Dual action solenoid

    setPosition LEFT

This sets the solenoid to turn on the left side only. Other possible parameters could be RIGHT, OFF and BOTH. (State)

##### Simple relay

    set ON

This sets the relay to the on position. If this relay is only one way, you would only have ON and OFF states. (Boolean)

##### Drivetrain

    controlWith Joystick1

This is likely not realistic, but provides an example of how you might provide a device as a parameter. (Device)
