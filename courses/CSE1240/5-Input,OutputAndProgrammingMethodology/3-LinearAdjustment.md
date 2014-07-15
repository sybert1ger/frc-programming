---
title: Linear Adjustment
layout: coursepage
---

Another, simpler form of feedback control is just linear adjustment. Effectively, this could be called PID without I and D.

Linear adjustment would be a control loop that changes it's output based on the current error. It would look like this:

    while (true) {
        setOutput(linearCoefficient * (setpoint - input()))
    }

This is a much simpler way of doing PID, and is equivalent to using PID with values of P = linearCoefficient, I = 0, D = 0.

Another form of linear adjustment is known as "bang-bang" control. This is the type of loop a heating system would have. If input is not equal to or higher than the desired input, than output is set to 100%. For a heating system, this works well. You keep it on at 100% until desired temperature is achieved.

You can use this technique whenever momentum is involved. If affecting the system will have a reoccurring effect (like heating a room, or spinning a wheel) then you can save power and make "spinup" time faster by using a bang-bang algorithm.

    while (true) {
        if (input() < setpoint) [
            setOutput(100)
        } else {
            setOutput(0)
        }
    }

A full version of bang-bang control is available [here](https://github.com/Team4334/atalibj/blob/master/src/edu/first/module/controllers/BangBangController.java).
