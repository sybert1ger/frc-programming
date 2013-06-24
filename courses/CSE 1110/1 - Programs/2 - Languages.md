---
title: Languages
layout: coursepage
---

We need instructions for computers to run. But how exactly do we write these instructions? Surely, computers cannot fully understand the English language. For that reason, we need something called a *programming language*.

Programming languages are very (eerily) similar to verbal languages. The only real difference is that they are not meant to be pronounced verbally. They all have ways of saying things, special words to represent things, and a specific way of interpreting them (like a dictionary).

Now, we don't mean to confuse you. A programming language's actual usage is very different from something like English. Programming languages are ways of telling the computer to do something, where verbal languages do many more things.

Some key principles that most programming languages use:

- Easy to read
- No verbose or extraneous language
- Simple, compact and succinct

Obviously, these principles are sometimes broken. All languages have their little quirks and weird behaviours. This is because they are all very large, and when projects are large some things are overlooked or ignored to stay on track. A "perfect" programming language is just too difficult to manufacture.

Some example languages that are commonly used today (started in):

- C (1972)
- C++ (1983)
- Java (1995)
- Python (1991)
- Javascript (1995)
- Ruby (1995)

All of these languages are very different from each other. They are all popular for different reasons. Usually, there is a standard language for solving a certain kind of problem, to eliminate incompatibilities between them. (Obviously others exists, but a vast majority of programmers use the same language) As you can see, popular languages have been around for a long time because it takes time for people to learn and master them.

# Platforms
A key difference between programming languages is the platform they are meant for. All of the programming languages listed above are **cross-platform**. This is a huge advantage for a language to have, since there are so many different platforms around.

So what is a platform? Platforms are things like:

- Operating Systems (Windows 7, Mac OSX, Ubuntu)
- Desktop Environments (Luna, Aqua, GNOME, KDE, Openbox)
- Frameworks (.NET)
- Graphics engines (Nvidia, AMD, OpenGL)

They are things that make programs compatible with the system.

Most of the time, programming languages are only compatible with some platforms. There needs to be special programs written to make code executable on some platforms.

# Syntax
A distinguishing part of programming languages is their syntax. Most programmers use syntax to differentiate between languages, because it is the biggest factor in writing programs in a language.

Syntax embodies:

- Rules of how symbols are interpreted by the computer
- Ways to perform certain actions
- Reserved keywords
- Ways to define data in different ways

As an example, here is python syntax:

    print("Hello World")
        
And here is some C code doing the exact same thing:

    #include<stdio.h>

    main()
    {
        printf("Hello World");
    }
    
As you can clearly see, there are some very stark differences between them.

In this course, the code that you'll see is written in python. It is the easiest to understand and write for new programmers.

# Execution
Interestingly enough, a programming language will become completely irrelevant after **compiling** a program.

Compiling is the process of taking the pure text of the code, and transforming that into something that the computer can understand and execute. The advanced syntax of modern languages is just too complex for a processor to execute by itself. There needs to be a conversion between the original code and an executable file.

Not all programming languages are directly compiled though. In fact, only 2 of the languages (C & C++) listed above are ever compiled into executable files. Most modern languages are even farther abstracted, and are run on **virtual machines**. You'll learn more about them later.

When comparing different executable files, the language they were written is completely stripped away. A C compiled program could be identical to a Haskell compiled program. It's unlikely, but the key is that executable files are not special from each other.

Executable files can also usually only run on certain platforms. They usually rely on certain parts of the system to be there. That is why there are different downloads for different operating systems, even if the program is the exact same on all platforms.

### Source vs Machine code

**Source Code** = The original code written in the programming language
**Machine Code** = The transformed code that computers can execute easily
