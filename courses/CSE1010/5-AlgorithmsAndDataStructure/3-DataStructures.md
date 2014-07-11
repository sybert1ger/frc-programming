---
title: Data Structures
layout: coursepage
---

We'll explore some of the basics of data storage. Note that this is not referring to file storage or databases, but rather the way that programs deal with specific programmatic data.

### Lists, Sets
Lists are variable sized data structures with unlimited capacity. Two well used kinds of lists are array-backed lists, and linked lists.

Array-backed lists use an internal storage mechanism that indexes data. Effectively, this means that data is stored and accessed using a number that represents where that element is in the list.

Linked lists are different in that they store one "node". A node contains an element, and a link to the next node in the list. Effectively, each node is linked to the next. This makes navigation through the list easier, but access to specific nodes more difficult.

Sets are like lists, but do not contain duplicate elements.

### Arrays, Tuples
Arrays are fixed-length data structures that contain a specific type of data, and index that data in the same way as lists. Internal data can be edited, but length is fixed. Tuples are effectively the same, but data cannot be edited.

### Maps, Tables, Dictionaries
Maps, tables and dictionaries use "keys" to access and store data. A piece of data is inserted with an accompanying key, and can only be accessed using that key. Usually, keys are strings of characters.

### Synchronized Data Structures (Vectors, etc.)
Some data structures are variants of others, but are "thread-safe". This indicates that multiple threads can concurrently access and change the data inside the structure without any side effects. Of course, timing of edits will still result in the most recent update being the current value, but that is a programmer's mistake to make.
