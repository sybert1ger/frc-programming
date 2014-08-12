---
title: Programming Languages
layout: coursepage
---

[CSE 1110](/courses/CSE1110/1-Programs/2-Languages/) gives a good introduction to the technicalities that define programming languages. Here, we will examine exactly what it means to *be* a programming language, and look at examples.

To see the vast variety of languages available to you, try this game:
[external link](http://helloworldquiz.com/)

<iframe src="http://helloworldquiz.com/", width="100%", height="500px"></iframe>

See if you can beat our high score of 2000 (no cheating!)

# Differences
### Functional, Imperative
<div class="video-container">
<iframe width="100%" height="450" src="//www.youtube.com/embed/sqV3pL5x8PI" frameborder="0" allowfullscreen></iframe>
</div>

### Syntax
Look at the differences of a simple printing statement between these two languages:

**Xtend**

    package sample

    import java.util.List

    class Greeter {
      def greetThem(List<String> names) {
        for(name: names) {
          println(name.sayHello)
        }
      }

      def sayHello(String name) {
        'Hello ' + name + '!'
      }
    }

**FORTRAN**
    
    program helloworld
         print *, "Hello, world!"
    end program helloworld
    
As you can imagine, these languages are built for entirely different things.

Interestingly, over the last 30 years a standard has slowly gained popularity. [C-based languages](http://en.wikipedia.org/wiki/List_of_C-based_programming_languages) are now extremely common. Almost every modern programming language still in use has remnants of the C language.

Directly or indirectly, everything follows from C.
