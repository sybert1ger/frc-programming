---
title: Activity - Sensors
layout: coursepage
---

To complete this activity, you will need:

- 1 5V Battery or Power Generator
- 1 Rotational Potentiometer rated for >= 5V ([ex](https://solarbotics.com/product/rt10k_t/))
- 1 Hall Effect Sensor rated for >= 5V ([ex](https://solarbotics.com/product/35055/))
- 1 Magnet
- 1 Multimeter

Your job is to measure these two devices.

[Instructions to measure potentiometer](http://www.instructables.com/id/How-to-measure-resistance-of-a-Potentiometer/)

### Instructions to measure hall effect sensor

1. Connect pin 1 on hall effect to +5V on battery (anything from 5V to 20V is fine)
2. Connect pin 2 on hall effect to 0V on battery
3. Connect a 50K resistor from +V to pin 3 on hall effect.
4. Using a multimeter, measure the voltage between pin 2 and 3 while you bring a magnet close to the device.
5. If you see a state change (i.e. a swing from almost 0 to almost the full supply voltage), the device is working.

Hall effect sensors measure polarity of magnetism, and turn on and off when polarity is reversed.
