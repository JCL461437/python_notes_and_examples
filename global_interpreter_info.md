# Pythons Global Interpreter Lock (GIL)

This is exclusive to python. This says that any thread that wants to be executing needs to acquire the interpreter lock. 

What this technically means is that we can only execute 1 thread at the same time regardless of your CPU core quantity.
In your computer you have a CPU that has multiple cores. Each core can execute one operation at a time (there are methods to increase this with hyper-threading but that is outside the scope of this)
With multiple cores you CPU can work on multiple things at the same time. Multi-threading comes in here. A thread is a component of your application thats being executed by the CPU. 
Larger applications (multi threaded applications) will have different pieces of code separated into different threads such that they can be executed at the same point in time.

With Python you can have multiple threads, but you have the GIL. What this means is that regardless of the CPU count on your computer, only one thread can be executed at a time.
Thats because the thread has to acquire something called the "lock" on the interpreter. Multiple threads are not going to increase the speed at which you execute your code. 

This means that separating computations across numerous cpu cores will not hasten your calculations. 