---
title: Sound
layout: coursepage
---

You might know sound sensors as **microphones**.

    In the magneto-dynamic, commonly called dynamic, microphone, sound waves cause movement of a thin metallic diaphragm and an attached coil of wire. A magnet produces a magnetic field which surrounds the coil, and motion of the coil within this field causes current to flow.
[Source](http://artsites.ucsc.edu/ems/Music/tech_background/TE-20/teces_20.html)

Essentially, a small metal piece vibrates from the sound, and using electromagnetism, changes the current. This change is amplified electronically, because the actual vibrations are too small to effectively change a current.

There are different ways that people use sound sensor devices.

1. Detect the presence of sound
2. Detect the frequency of sound
3. Record the entirety of sound

\#2 and 3 might look similar, but can be dramatically different. Think about #2 as a guitar tuner, and #3 as a full microphone.

Detecting the presence of sound is a much less expensive device - any vibration will amplify the current to a certain level. Typically, the circuit is such that only "volume" is measured.

Detecting frequency is almost as complicated as recording the exact sound, with the exception of the shortcuts that one can make internally. With our example, a guitar tuner, you can imagine that instead of building a processor that handles the signal, we could simply build logic circuits that detect the signal and activate individually depending on the signal (eg. C# turns on the "C Sharp" circuit and displays on screen).

Recording sound is a different process, because the usual setup is a "dumb" microphone - meaning that the actual device has no advanced circuitry, it simply transmits vibrations. This could be less expensive that #2, except for the fact that the expensive part is making that signal useful (computer, recording device, etc.)
