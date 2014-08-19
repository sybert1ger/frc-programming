---
title: Feedback Loops
layout: coursepage
---

In [ELT2080](/courses/ELT2080/1-ControlSystem/3-ControlLoops/) you relooked at control loops. Let's examine a specific example of control loops - feedback loops.

Feedback loops are [closed loop](/courses/CSE1240/5-Input,OutputAndProgrammingMethodology/1-ControlLoops/), and always use measured output that is effected by the output of the system.

How do feedback loops enter into simulation and process control? They are one of the main elements of a system that need to be examined, studied, tuned and simulated. Because of their complicated and uncertain nature, we want to get a good grasp of them before implementing them on real world systems where they can cause damage. For this reason, simulation of feedback loops is popular in systems engineering and embedded programming studies.

Unfortunately, simulations of feedback loops are extremely difficult to implement. This is because a simulation requires you to take into account physics, randomness and noise in the signal. All three of these are difficult challenges on their own.

Here are some examples of simulators:

[PID simulator](http://sourceforge.net/projects/pid-simulator/)

[PID Loop Simulator](http://www.engineers-excel.com/Apps/PID_Simulator/Description.htm)

[PID Loop Optimizer](http://www.expertune.com/PIDLoopOpt.aspx)

[On-Off Control simulator](http://www.engineers-excel.com/Apps/OnOff/Description.htm)

![](/img/pid-sim.jpg)
