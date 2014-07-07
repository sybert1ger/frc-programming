---
title: Motor Control
layout: coursepage
---

There are two ways to adjust the speed and torque of an electric motor. One is to adjust the actual voltage. This adjusts how much power the motor has, and in effect changes the speed. This method can be inconsistent, and can have negative effects on the motor's life.

The second way to adjust speed is more accurate and has more torque, but requires more complex control. It involves turning the electricity on and off very quickly, creating the adjustment of speed. This gives the motor the same amount of power, with control over the speed. This form of control is usually done through [pulse width modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation).

# PWM
At the core of PWM is the signal. Although the way that the signal is interpreted is very important, it's irrelevant to PWM theory.

<iframe width="560" height="315" src="//www.youtube.com/embed/YmPziPfaByw?rel=0" frameborder="0" allowfullscreen></iframe>

                        4 on - 2 off
    5V      ____    ____    ____    ____    ____
           |    |  |    |  |    |  |    |  |    |
           |    |  |    |  |    |  |    |  |    |
    0V   __|    |__|    |__|    |__|    |__|    |__
         0       1       2       3       4       5
        
You can see that the power is on 4 times out of 6 in one millisecond. This is basically 66% speed, or average 3.3V.

If you wanted to go at 20% speed, the calculation would be:

    20% = 0.2
    1 / 0.2 = 5
    
    1 out of every 5 times

Which would produce the signal

                        1 on - 4 off
    5V        _      _      _      _      _
             | |    | |    | |    | |    | |
             | |    | |    | |    | |    | |
    0V   ____| |____| |____| |____| |____| |____
         0      1       2       3       4       5

This looks like 20%.


           1 on - 0 off
    5V   ________________ 
        
    0V   
         0  1  2  3  4  5

Remember that these diagrams are being shown on different scales. The first diagram had 5 counts per millisecond, while the second had 5 and the last only had 1.
