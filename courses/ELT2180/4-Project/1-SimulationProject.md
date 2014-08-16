---
title: Simulation Project
layout: coursepage
---

For your simulation project, we will do a simple robot movement simulation. This is in no way realistic, but it gives you an idea of how you can use simulation to determine real-life behaviour. We understand that it is actually quite useless, but of course, a useful simulation would require a lot more complexity and programming.

####[Download](http://github.com/frc-west/tasks-simulator/releases)
Find the "Latest release" and click the "TasksSimulator.jar" green button.

####[Install](https://netbeans.org/downloads/)
Download the "Java SE" bundle. Follow instructions to install.

After installing, open netbeans.

1. Click "File -> New Project..."
2. Click "Java" under categories, and click "Java Application" under projects. Click next.
3. Under project name, put your full name. Click finish.
4. Your project will show up on the left side. Right click "Libraries" and click "Add JAR/Folder". Chose the "TasksSimulator.jar" file that you downloaded earlier.

Now, you can copy and paste the following code in the file open in the main window.

    import com.frcwest.TasksSimulator;

    public class YourNameHere {

        public static void main(String[] args) {
            TasksSimulator simulator = new TasksSimulator(10, 10);
            simulator.dieWhenFinished();

            simulator.addMoveRobot(1, 0);
            simulator.addMoveRobot(6, 0);
            simulator.addMoveRobot(0, 3);

            simulator.start(2);
        }
    }

Replace the "YourNameHere" as your name. You should be able now to click the green arrow up top, to run the program.

Alright, hopefully you've made it this far. I'll explain a little bit about what this program is doing, and what you can do with it.


    import com.frcwest.TasksSimulator;

    public class YourNameHere {

        public static void main(String[] args) {

Basically, you can ignore these lines. They are simply there to tell Java what you're doing and how you're doing it.

    TasksSimulator simulator = new TasksSimulator(10, 10);
    simulator.dieWhenFinished();

These lines do two things. First, `new TasksSimulator(10, 10)` tells it that your grid will be 10x10. You can change these numbers to whatever you want, although you will start to see problems when giving higher numbers.

Secondly, `dieWhenFinished()` tells the program to quit after the simulation is done. You can remove this entire line if you'd like it to remain open until you manually close it.

    simulator.addMoveRobot(1, 0);
    simulator.addMoveRobot(6, 0);
    simulator.addMoveRobot(0, 3);
    
As you can imagine, these lines tell the simulator that it should do those three things. `addMoveRobot(1, 0)` moves the robot 1 space to the right, and 0 spaces down. You can use negative numbers here.

You can add as many of these movements as you want. If a movement forces the robot to hit a wall, a small `Stopped by a wall!` message will appear in netbeans.

You can also add printing statements, so you know where the program is in execution.

    simulator.addPrint("Your message here!");

Lastly, we start the simulation.

    simulator.start(2);
    
This will start the window and execute your instructions. The `2` is how many seconds to delay between instructions. You can change this to any decimal value.

## Objective
Your objective is to do 5 things.

1. Have the robot touch each 4 of the corners.
2. Have the robot touch the centre tile.
3. Have the robot say "hello" twice, in different tiles.
4. Never touch the same tile twice.
5. Return back to the starting position at the end.
