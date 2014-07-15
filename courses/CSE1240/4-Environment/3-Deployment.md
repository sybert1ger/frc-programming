---
title: Deployment
layout: coursepage
---

When talking about embedded systems, especially robots, deployment process is an important consideration.

It's such a large topic, that we can't talk about any kind of specifics. Instead, let's focus on the methods and strategies used.

### USB / Digital
Most small platforms use a small "image" file that is deployed over a serial bus into the flash memory on the control system. Arduino and the roboRIO are examples of this form of deployment. Typically, there is a handshake process involved in doing this - the computer will "ask" the robot to stop everything and let a new image in.

This process also depends on how the robot code is run on the platform. If there is a kernel and operating system running below the user code (meaning your code is run on the application layer), it is a simple process to change the code - you basically just replace an old file with your new one.

If your code is very low-level, and there is nothing being run underneath, the process could be much harder. Your computer will likely have to take control of the internal memory on the robot, and change the data there to the new program you're deploying.

![](/img/arduino-deploy.png)

### Network connections
If the platform you are deploying to is complicated enough, it may actually be it's own server. In effect, the user would connect to the server and send the new files over that connection. This is a much safer option, because a disruption in connection won't necessarily break any deployment progress.

It's worth noting that this method is used for the cRIO and roboRIO, and that it is highly recommended to use a wired connection to do so. Although a deployment failure will likely be a non-issue, it can be annoying to deal with slower and less reliable connections.

![](/img/deploying-code.jpg)
