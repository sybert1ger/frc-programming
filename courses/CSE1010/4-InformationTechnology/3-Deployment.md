---
title: Deployment
layout: coursepage
---

There are a lot of steps between writing code and having that code end up on other people's computers around the world. As a matter of fact, something very different is sent.

There are different disciplines of programs and deployment, so we will go over the basics.

## Compiling, Building and Running
Before a program can be given to anyone, a conversion needs to be done. This conversion is different depending on what programming language you are working in. Traditionally, we talk about *compilers*. These are small programs that are able to convert the text you've written into machine code.

Compiling is not where things end, however. As a program becomes more complex, extra steps might need to be taken to build and test. Building is typically the process of compiling the correct files and putting them in a logical structure which is ready to install.

Once the program is ready, installing should be as easy as moving files to the correct place. Sometimes, this process might also involve changing registry values or configurations of other programs.

#### Packages
Package managers make the building and installing process easy for a user. Because every program has wildly different requirements of installing, making a standard for doing this process is desirable.

This shifts the burden of installing to the developer, which in a lot of ways makes life easier for everyone.

## Distribution
Generally, distribution of software has gotten easier over the years. Things like package managers with central repositories for packages have been a blessing for developers. There are a variety of kinds of these repositories, including [debian repositories](https://www.debian.org/mirror/list), [app stores](http://windows.microsoft.com/en-ca/windows-8/apps), etc.

The internet has helped make distribution easy. In the past, tapes and CDs were the only way to get software on your computer, imaginably inconvenient.

## Website deployment
There are basically two different kinds of websites. Static (like this one) websites are relatively simple. Their content never changes, as long as nothing new is uploaded to the server. In theory, they are similar to a file server that just returns what file you asked for. There is no interactivity with the webpages, and generally they are more secure because of that.

The other kind is a dynamic website. From a user's perspective, you may not even notice if a website is dynamically generating content. Something like google (search engine) is a perfect example of a dynamic website - everything changes according to your needs and what you ask it.

[Docker](http://www.docker.com/) is an example of a way to deploy web services and applications. This topic is expansive and far beyond the scope of a beginner's understanding.
