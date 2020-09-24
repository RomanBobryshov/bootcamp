#### What is the purpose of decorators?
***

###### Decorator
First of all, I would like to say that decorator is a design pattern in Python. That allow to add new functionality to object without modifying structure. Decorators are usually called before the definition of a function you want to decorate.

Decorator needed when a piece of code is used a large numbers of times. For example, a function for caching the result of another function.

Need to understand that decorators like all functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object in python.

Summarizing I can say that the decorator is a function that takes in a function, adds some functionality and returns it.
