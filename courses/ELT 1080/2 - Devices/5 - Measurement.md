---
title: Measurement
layout: coursepage
---

To read signals from sensors, oftentimes you need something in between the sensor and the processor. This device measures the sensor's actual signal, and converts it into something useful for the processor.

These devices are essential to a system, because they allow all kinds of sensors to be useful. Otherwise, the load put on a processor might actually render it useless for other tasks, which is exactly what we don't want.

### The DAC (Digital to Analog Converter)

![](http://upload.wikimedia.org/wikipedia/commons/b/b1/8_bit_DAC.svg)

The DAC is one of the building blocks of almost all modern music machines. At a basic level, DACs convert a digital signal into an analog one. In practicality, this makes speakers, screens and many other analog devices possible. These devices are necessary because of the nature of processors. Everything is dealt with in digital signals, because varying voltage isn't important to it.

For a speaker, however, it is. A digital audio file must be converted to the speaker's signal, to play in real life.

Ideally, a DAC will reconstruct an analog signal. Basically, this means that the signal is "smoothed".

![](http://upload.wikimedia.org/wikipedia/commons/8/88/Sampled.signal.svg)

But, some simpler DACs will only directly convert a signal.

![](http://upload.wikimedia.org/wikipedia/commons/1/15/Zeroorderhold.signal.svg)

As you can imagine, a DAC has very specific requirements for encoding of signals. In other words, the digital signal must adhere to a preset standard for data.

Often, when manually checking data signals, you will use a DAC. This allows you to analyse the digital signal in an understandable way (1 decimal number versus 8 bits). You might vouch to use a computer instead and just look at the signal with a computer, which wouldn't require a DAC.

### The ADC (Analog to Digital Converter)
Used more commonly in electronics is the analog to digital converter. This is used more often because the natural world lends itself to analog signals. It's difficult to find a real world phenomenon that is measurable as a digital signal. Most of the time, it is a variable number.

A processor's power is wasted trying to measure voltage and convert to a binary number. For this reason, we use very specifically designed chips to do this itself. This way, it is more efficient and better for the processor.

Something worth noting about ADCs is that they will not always be perfectly accurate. Often times, software and hardware combine to give inaccurate results. For this reason, there can be small [noise](http://en.wikipedia.org/wiki/Noise_\(electronics\)) in the digital signal.
