---
title: API Spoofing
layout: coursepage
---

API "Spoofing" is not a proper term, but rather an explanation of what really goes on in emulation.

Let's say that there is a robot that has 3 different controls:

    1: Control of the forwards / backwards movement
    2: Control of the side-to-side movement
    3: Movement of a simple arm
    
And we want to emulate this robot somehow. Well, first we would need take note of how we currently control the robot.

    1: Program has a method called "move(speed)"
    2: Program has a method called "turn(movement)"
    3: Program has a method called "arm(speed)"

So, we can theoretically take any user program that's already been written and drop it in an emulation that provides those three methods in some way.

The robot's controls would be known in this case as its API, and the program would be known as a user application. The emulation is a "virtual machine", basically being a **spoof** of the API.

A normal operation looks like this. Input goes into an API and directed to robot controls.
![](/img/normal-api.png)

A spoofed API "redirects" input from the API into an emulator.
![](/img/spoofed-api.png)
