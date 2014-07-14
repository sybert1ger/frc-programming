---
title: Embedded Systems
layout: coursepage
---

When talking about programming robots, generally we are talking about **embedded systems**. This effectively means that the system is dedicated towards one purpose, and the processor is *embedded* as part of the complete device.

Embedded systems are everywhere around the world, they are your microwave, watches and cars. Anything with a microprocessor that has a specific and non-changing role is an embedded system. Generally, embedded systems are non-flexible.

Robots are great examples of embedded systems because they have specific purposes, but are also powerfully adaptive.

Programming embedded systems is a lot different than programming on general purpose PCs. This is because, by definition, you are writing software that cannot crash or fail safely. And to add to that, most of the time, you are working with low-level hardware that has not smart handling of information - whatever input you give something, it will do that.

You could argue that programming in FRC is far removed from "real" embedded system programming. Considering how many layers of software are doing the hard work underneath your application logic, it might even be appropriate to call your FRC programs applications run on what is effectively an operating system.

This is both a good and bad thing. For one, you get to worry more about functionality than re-inventing the wheel. But at the same time, much of the difficulty and subsequent challenges are removed. It's up to you to decide if you like how easy things can be.

But we won't worry about the technicalities of libraries, virtual machines, etc. when discussing embedded systems. In effect, your program is still "embedded", and would be considered as such by any reasonable person.
