---
title: Programming Language
layout: coursepage
---

The programming language to write robot programs in is a very different decision compared to something like desktop applications. There are a lot of extra concerns to take into account, not only preference.

#### Is the language safe?
This is a crucial question to ask about embedded programs, because there isn't room to "fail" or exit unexpectedly. What does safe mean though?

It's simple enough - usually a safe language will have these qualities:

- Type-safe / strict type (helps with invalid casting errors)
- Generics (helps spot errors or bad practices during compile time)
- Good error handling (able to deal with something going wrong)
- Strict compiling rules (find problems before they show up in real life)

Mostly, safe languages will force you to do things correctly - it won't allow you to hack around.

#### How fast is the language?
Performance can become an issue in embedded programs if you have real expectations about how quickly the system needs to react. Realistically, performance issues will largely depend on your platform of choice.

For example, Java would be considered as a poor choice for embedded programming. This is because of it's need for a virtual machine, garbage collection and byte-code dependance. There are simply too many layers needed to run Java code to call it a well performing language. But, if you have a capable processor with enough memory, Java can (and has in FRC) become a valid option.

#### Compile times and deployment
An immediate selling point of languages like C is that compiles times can be very good. This helps in preventing wasted time.

Ease of deployment is also a huge concern for any human being. If there are a lot of steps just to get your code to run, you are much less likely to consider the language a good option. Usually, you can find tools and techniques to make deployment easy, but it's no guarantee.

## Common Options
To anyone with experience, **C** or **C++** are obvious answers to "What programming language to use?" in embedded systems. And they're right - it is extremely well suited to the task. C's low-level access to system calls and hardware is extremely important to most embedded applications.

Some further options:

- [RobotC](http://www.robotc.net/)
- [Labview](http://www.ni.com/labview/)
- [Arduino](http://arduino.cc/en/Main/Software)
- [Lego Mindstorms](http://www.lego.com/en-us/mindstorms/downloads/software/ddsoftwaredownload/)

You can find many different C derivatives that are designed for a specific hardware platform.

In FRC, Java, C++ and Labview are all well used options.
