---
title: Sensor Feedback
layout: coursepage
---

Sensors are, as you know, a big part of the robotic control system. You explored a few different kinds of sensors - let's look at examples of uses for these sensors and how their input is utilized.

#### Photoelectric
You can use photoelectric sensors for two things.

1. Find out if an object is present
2. Find the distance to another object

The first option might not initially make sense. So let's look at an example.

<div class="video-container">
<iframe width="100%" height="450" src="https://www.youtube.com/embed/JSj-OAiwRNg" frameborder="0" allowfullscreen></iframe>
</div>
<p>
When picking up the second ball, the robot needs to know when the ball is actually in the claw. This likely (and in this case does) uses a photoelectric sensor to check this "possession" of the ball.

#### Sound
Sound sensors are harder to find direct uses for. They are not entirely useful by themselves to observe the environment. But, voice control is a very powerful tool found in a lot of modern phones. And if you are looking at simpler solutions, "tapping" or sudden noises can be used for control. By making an abrupt noise every time you want your robot to turn, you might be able to keep it on a straight path. Admittedly an inefficient solution, there still might be other more useful applications.

#### Tactile
Looking back at the first example of the two ball autonomous, a tactile sensor might be extremely useful. Instead of detecting the presence of the ball with a light, you can use a small button. The ball would press the button when inside the claw, and you have an equally effective sensor (at a much lower cost).

#### Proximity
In the autonomous example, you might want to drive up to the wall. To do this, you might not want to rely on floor distance or motor speed. You might want a foolproof way to stop before the wall. A proximity sensor would work well for this, especially since you can start slowing down as the sensor tells you that you are getting closer.

#### Thermal
Thermal sensors are either useful to solely know the temperature, or a regulatory reason. Of course, you understand the reason to know the temperature. But as a regulating device, thermal sensors are useful. For example, a gyroscope is a sensor that is largely affected by the temperature of the external environment. You can, however, adjust the signal according to what the temperature is.
