---
title: Libraries
layout: coursepage
---

A really cool part of programs is their ability to use code from other programs. These other programs are known as "libraries", or "dependencies". They are used to make complex tasks easier.

You might want to display a window on the screen with a program. To do so, you would use libraries, like so:

    Ask Operating System for graphics manager
    Ask Graphics Manager for window space
    Ask Graphics Manager to render a screen on the window space
    Graphics Managers asks Renderer to process the screen
    Screen is displayed

So instead of having to write really low level code to display pixel by pixel, you can ignore the details of how it's done and only worry about what to display.

There are also usually programming language libraries. For example, python has a large assortment of libraries to do anything you want. This makes things much easier for the programmer, so that they don't need to worry about details.

This is all known as low-level abstraction. This simply means that the hard-to-do details are taken care of for you, and you just need to provide input.

You will probably be unknowingly using a lot of libraries when programming. They make everyone's life easier, because re-writing already established code is tedious and a waste of time. We are building on the shoulders of giants.

## Finding libraries
Libraries are usually found online. Many libraries have been written in the past few decades, and are found for a variety of languages, platforms and locations.

For python, see [UsefulModules](http://wiki.python.org/moin/UsefulModules) and the [python standard library](http://docs.python.org/2/library/) for more information.

### Examples
- [OpenSSL](http://www.openssl.org/) Cryptography library for encryption, secure connections, etc.
- [Guava](http://code.google.com/p/guava-libraries/) Java libraries for general purposes
- [jQuery](http://jquery.com/) Javascript library to make readable and compatible code
- [matplotlib](http://matplotlib.org/) Charting and plotting library for python
- [RevealJS](http://lab.hakim.se/reveal-js/#/) Presentation library in javascript
