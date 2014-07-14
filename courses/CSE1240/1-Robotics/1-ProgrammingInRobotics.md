---
title: Programming in Robotics
layout: coursepage
---

You now have a grasp of basic programming concepts and how to use them in a structured environment. We will now move on to how this fits in with robotics, and what changes in that context.

We will use FRC programming as a reference for robotic programming, as it will provide a good example and prove useful in the future.

So what's different about programming robots? That question leads to a lot of other, more detailed questions like "What kind of robot?" and "What is the function of the robot?". In reality, saying "programming in robotics" is almost as valid as saying "construction of roads". You get a general idea what the goal is, but there is still a lot to be explained before you can get close to accomplishing what you want.

Let's assume that programming robots is a generally specific process, provided:

- The robot in question has limited processing power
- The robot has analog and digital input/output
- Your goal is to make movement based on various sources of input
- You deal with hardware in a slightly abstracted way (libraries, virtual machine, etc.)

Now that we have a better idea of what we're dealing with, we can start to imagine what the program looks like.

- Small and compact processing, only performing necessary actions
- Uses input from sensors to provide output to motors, servos and actuators
- Uses control loops and algorithms to adjust movement
- Can make library calls to change output and receive input

And with this information, we can start to construct our idea of what a robot program might look like. Note now, that **Java** will be used for examples from now on. See [this](http://learnxinyminutes.com/docs/java/) page for Java syntax - you will need a few minutes to accustom yourself to the language. Don't worry much about classes or objects yet, as they are not heavily used here.

Let's make some assumptions about how the code will work:

- Runs in a loop continuously to update the state of output
- Uses input from a driver through a network connection
- Has settings to adjust behaviour that are adjustable either real-time or at compile time

Here's a simple example of robot code using the WPILIBJ libraries (2013).

    public class MainClass extends IterativeRobot {

        Joystick joystick = new Joystick(1);
        RobotDrive drive = new RobotDrive(1, 2, 3, 4);

        public void teleopPeriodic() {
            drive.arcadeDrive(joystick.getRawAxis(1), joystick.getRawAxis(2));
        }
    }
    
`IterativeRobot` is a class definition that contains "periodic" functions - they are looped during their respective game mode every 20ms. `teleopPeriodic()` does that exactly.

Joysticks is an object that gathers input from the Driverstation software - basically, it asks the laptop that is connected (through wifi) to the robot about the joysticks that are attached to it.

RobotDrive is an object that controls 2 or 4 [PWM](http://en.wikipedia.org/wiki/Pulse-width_modulation) outputs that should go to speed controllers that control drive motors.

Arcade drive is a driving control scheme that controls forward speed with one input, and turning with another input. This matches most video games, which is intuitive for drivers.

So, you can tell that this code is *very* far removed from what's happening internally on the robot. In fact, this is close to the highest-level programming possible on such a low-level platform.

The fact that you do not need to worry about network connections, PWM outputs, joystick drivers, looping semantics, game mode switching, port buses, analog output, timing or even driving algorithms is a huge weight off your shoulders. But, be careful. With such a huge amount of work done for you, you lose control over exactly what happens in your program.
