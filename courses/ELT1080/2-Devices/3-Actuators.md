---
title: Actuators
layout: coursepage
---

Part of a control system that we haven't described very well is the actual system that we are controlling. This is because the definition is very open. You could almost call anything a system. This isn't neccesarily a problem, but it does prevent some amount of understanding. Hopefully you can understand that the important part of "control system" is the "control". The system, although certainly important in real life, is not our concentration here.

But it's worth describing some examples of systems. Let's examine 3 examples.

### Speed Controllers
In many different areas, we would probably describe a system as some kind of motor or motor-controlled component. It's acceptable to think of "speed controller" as a motor, provided that you understand the difference between the two. Speed controllers adjust output to a motor based on a signal. Most used something called PWM (Pulse Width Modulation). This, simply, means that it turns the motor on and off very quickly. The more often that the motor is on, the higher the speed.

Speed controllers work like this:

![](/img/speed-controller.png)

SIG turns on and off very quickly, and the speed controller adjusts the OUT voltage accordingly (on and off).

### Relays
As you remember, relays turn a circuit on and off. What you probably haven't realized, however, is that the input can be a much lower voltage. This allows the user to send low-voltage signals to adjust a high voltage output. As a matter of fact, a relay diagram would look identical to the above speed controller. The only difference is that a relay is a mechanical device, where a speed controller is controlled electronically. The response time for a speed controller is much better.

So, why use a relay when a speed controller does the same thing better? Mostly, it's price. Speed controllers aren't inexpensive, while relays can be very cheap. This is because relays have very little circuitry - they simply pass on a signal using an electromagnet.

### Solenoids
Solenoids are controllers for pneumatic systems. Similar to relays, they use physical switches that get pushed (sometimes magnetically) from one position to another. This allows air flow to be controlled, and only go out of one output.

Solenoids come in many different configurations. You can get anything from simple spring-controlled single-action solenoids to 10-output systems with binary configurations.

Typically, a control system will use a simple circuit to change which output of the solenoid to use.

![](/img/solenoid-diagram.png)
