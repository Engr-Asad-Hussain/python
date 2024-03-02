### Concurrency Vs Parallelism
True parallel computing means that an application runs multiple tasks at the same time where each task runs as a separate processing unit. 
Concurrency means that an application is making a progress on more than one task at the same time but may switch between these tasks instead of actually running them in parallel. If an application works say on task A and B, it doesn't have to finish A before starting B, it can do little bit of A then switch to doing a little bit of B back again to A and so on so forth.

> This example on stackoverflow clearly states the difference:
"Concurrency is two lines of customers ordering from a single cashier (lines take turns ordering). Parallelism is two lines of customer ordering from two cashier (each line gets its own cashier)"
If you translate this back into computer language than cashier is a processing unit (A CPU Core). Each customer is a task that the processor needs to take care of. 

Modern computer use a combination of parallelism and concurrency. You CPU might have 2, 4 or 8 cors that can perform tasks in parallel. Your OS will runs tens to hunders of different tasks concurrently. A subset of those tasks are actually running in parallel while the OS seamlessly switches between the tasks.

### Python Global Interpreter Lock (GIL)
Parallelism in Python has caveat which is the Global Interpreter Lock (GIL). Anytime you run python code it needs to acquire a lock on the interpreter, which means that Python code is single-threaded even if you start multiple threads. There are ways around this for example by relying on multiple processes instead of multiple threads or by switching to another interpreter that doesn't have to lock.
Concurrency on the other hand works really well in Python specially since version 3.10. 

### The benefits of Concurrency
Why concurrency is smart way to do computing? Well it so happens that many involves waiting or applications are waiting for files to be read or written to. They are constantly communicating with other services over the internet or they are waiting for you to input your passwords or click a few buttons to help identify traffic lights (reCAPTCHA). It considerably speeds things up if a computer can do something else while waiting for that network response or for you to finish cursing about recaptchas in other words concurrency is a crucial mechanism for making our computers work efficiently in this age of connectivity.

The asyncio package in Python gives you the tools to control how concurrency is handled within your application - async and await are the keywards used to achieve this. If you write async keyward in front of a definition or function that its indicating you allowed to run this method or function concurrently. await gives you control over the order that things are being executed in. If you wirte await keyward in front of a concurrent statement this means that the portion written below that statement can only be executed after the concurrent statement has completed. Being able to do this is important when the next part of your code relies on the result of the previous part and this is often the case you need to wait untill you get the data back from the database or you need confirmation from the API that your user is logged-in in order to continue and so on.

Recap of asyncio in Python
I want to start with a quick recap of how concurrent programming in Python works. So for this you need to use async and await syntax. I have a simple example here that retrieves pokemon names, so I am using a free API here to do this. So as you can see here is a synchronous version of that code it's a function get a random pokemon name that picks an id between one and the maximum pokemon id that's available we have the url and we construct it

### Reference(s)
https://www.youtube.com/watch?v=GpqAQxH1Afc&t=296s&ab_channel=ArjanCodes