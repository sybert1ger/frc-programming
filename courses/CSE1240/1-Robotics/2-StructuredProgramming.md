---
title: Structured Programming
layout: coursepage
---

Programming can quickly become confusing if you are not entirely clear about what the program you're working on does. Writing programs in a structured and clear format is a valuable skill that will constantly pay its dues throughout your life.

Similar to writing, if other people can easily understand a program, more people will read and use it.

So what is structure in the context of programs?

- Organized and categorized elements
- Well defined and readable naming schemes
- Clear logic with correct formatting
- Consistent and obvious spacing
- Generally good programming habits such as defining variables in the correct scope

Let's examine these a little closer.

### Organized and categorized elements
This amounts to sorting the elements of a class in Java in a logically consistent way. Generally, you can follow this flow (don't worry about sections you are unfamiliar with)

    public class MyClass {
        public static final int VARIABLE = 1;
        public static int variable = 2;
        private static int privateVariable = 3;
        
        public final int VARIABLE = 4;
        private final int variable = 5;
        
        public MyClass() {
            // Constructor
        }
        
        public static void staticFoo() {}
        private static void privateStaticFoo() {}
        
        public void foo() {}
        private void privateFoo() {}
        
        public class InnerClass {}
        private class PrivateInnerClass {}
    }

You should be able to tell, even without understanding what each element is, that there is a structure. It follows a basic pattern - for example, static elements are always first.

The most important lesson to learn about structured programming in Java is:

- Declare variables at the top of classes
- Format spacing correctly (In netbeans, you can use Alt-Shift-f to do this automatically)
