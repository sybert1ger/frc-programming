---
title: Pneumatics
layout: coursepage
---

Pneumatics uses pressurised gas to move things. Simple circuits are created with a power source and switches, and can be used for thousands of different uses. Generally, pneumatics are well suited for tasks that require fast action and response time. Similarly to electronics, pressure can be regulated to specific points, giving control of the power of elements in a circuit.

There are various pieces that you can use in pneumatic systems:

- AND gates - Connects one power source to multiple outputs
- Regulators - Connects one power source to an output that has a maximum pressure
- Solenoids - Connects one power source to one output of many (controlled by electrical signal)
- Actuators - Things that perform actions based on pressure

### Solenoids
![](/img/solenoid.jpg)

Solenoids use an electric signal to determine which output to use. They are useful for controlling actuators, like pistons. To understand solenoid diagrams, visit [here](http://www.solenoidvalvesuk.com/solenoidsymbols.asp).

### Pistons
![](/img/cylinder.gif)

A pneumatic piston or cylinder is controlled using one or two inputs (image has two). A single input would indicate that the cylinder is spring loaded, and without pressure defaults to a position. A dual input means that the cylinder is pushed from both sides. The side that more pressure is applied to will push out. Inputs are found at each end of the solenoid.

# Motion
Motion in a pneumatic system is created by pressure somewhere in the system. This power source is typically either a [compressor](https://en.wikipedia.org/wiki/Gas_compressor) or a pressurised gas tank. Both of these have higher than normal pressures, and push air through the system.

### PSI
PSI (Pressure per Square Inch) measures how much pressure there is in a system. PSI needs to be regulated to avoid safety hazards including explosions. Equipment is only rated for certain pressures, and higher pressures are dangerous.

<table class="table table-bordered">
    <thead>
        <tr><th>Device</th><th>Normal PSI</th></tr>
    </thead>

    <tbody>
        <tr><td>Bicycle Tire</td><td>65</td></tr>
        <tr><td>Water Jet Cutter</td><td>40,000 - 100,000</td></tr>
        <tr><td>Scuba tank</td><td>3000</td></tr>
    </tbody>
</table>
