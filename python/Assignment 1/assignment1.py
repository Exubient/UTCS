"""Assignment 1

Get yourself started with a development environment and write some
code and look at the Python documentation.

For 90%:
* Fill in the fac function with an implementation of the factorial
  function.
* And the fib function with an implementation of Fibonacci.
* And the linear_fib function as it's documentation specifies.

For 100%:
* Implement fac on one line using one standard library function and
  the product function below. Look up the range function.

None of your code should print any output. If you want to have some
debugging prints you do not have to remove, look up and use the
logging package in the standard library.

See:
https://docs.python.org/3/library/functions.html

Feel free to use any code you find in the Python documentation. 
However you should cite the source of the code in a comment.

"""
"""
UID:hk23356
Name: Hyun Joong Kim (Henry)

"""
import functools

def product(l):
    """Compute the product of all elements of the iterable l."""
    def times(x, y):
        return x * y
    return functools.reduce(times, l)

def fib(n):
    """Compute the n-th Fibonacci number.


    Note: fib(0) is 0, and fib(1) is 1.
    """
    if n < 0:
        raise NotImplementedError		
    elif n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fac(n):
    """Compute n! (n factorial).

    Note: fac(0) is 1.pp
    """
    if n == 0:
        return 1
    else:		
        return n * fac(n-1)

cache={} #fibo cache for the problem

def linear_fib(n):
    """Compute fib(n) in O(n) time using memoization.

    Use a global variable and one of the data structures you have
    learned about to implement a linear time recursive Fibonacci. Use
    memoization; it is possible to implement Fibonacci in linear time
    without memoization (using a loop), but that is not the
    assignment.
    """
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            cache[n] = n    
        else:
            cache[n] = linear_fib(n-2) + linear_fib(n-1)
        return cache[n]



