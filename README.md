# Week 10


### Object-Oriented Principles

This week we start by learning about _inheritance_, one of the three prongs of object-oriented programming.  The other two are _encapsulation_ and _polymorphism_.

Encpasulation is an object's ability to hide its internal state from other objects.  Traditional OO programming expects objects to expose only methods, not data.  As you've seen this quarter, Python does not adhere to this principle in the least.

Polymorphism is a way to transparently substituate one object for another, in order to gain different behavior depending upon circumstance.  In statically-typed languages, polymorphism can only be achieved through inheritance.  In dynamically-typed languages, inheritance plays a far smaller role, because polymorphism can be achieved by "duck typing" and other method-specific behavior.


### Introduction to Statically-Typed Languages

Next, we will use the online Java compiler at https://repl.it/languages

Or we might use the one at http://www.tutorialspoint.com/compile_java_online.php

Quick overview of statically-typed languages:

* All variables must be declared before use
* All variables must strictly declare their type before use
* Once declared, variables cannot change their type
* Nowadays, most languages that have been traditionally statically-typed have introduced dynamically-typed features and are blurring the lines quite a bit.
* All programs require a _compile_ step, which turns the source code into machine language (or an intermediate representation called _bytecode_.)  Once the code is compiled, you can execute the compiled program.  If you change the source code, you have to compile again.
* If the compiler generates bytecode instead of machine code, the resulting program must be run by an interpreter or "virtual machine", often called a a "VM".  But a VM is just a fancy name for a program that runs your code for you, just like we've done with `python3`.



### Unix Commands You Should Know

We will use unix.txt as a review guide.  I also recommend taking the "Unix Bootcamp" offered by the MPCS every fall.


### Wrap Up

I hope this quarter has been the start of something great for you!
