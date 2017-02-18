"""
Assignment 4: Metaprogramming

The idea of this assignment is to get you used to some of the dynamic
and functional features of Python and how they can be used to perform
useful metaprogramming tasks to make other development tasks easier.
"""

import functools
import logging
import sys

def logcalls(prefix):
    """A function decorator that logs the arguments and return value
    of the function whenever it is called.

    The output should be to sys.stderr in the format:
    "{prefix}: {function name}({positional args}..., {keyword=args}...)" 
    and 
    "{prefix}: {function name} -> {return value}"
    respectively for call and return.

    Look up functools.wraps and use it to make the function you return
    have the same documentation and name as the function passed in.

    This will be used like:
    @logcalls("test")
    def f(arg):
        return arg

        (This is a more refined version of what I did in class)
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            arg_all_str = ",".join([repr(arg) for arg in args] + [item[0] + "=" + repr(item[1])for item in kwargs.items()])
            sys.stderr.write(prefix + ": " + func.__name__ + "(" + arg_all_str + ")")
            sys.stderr.write("\n")
            sys.stderr.write(prefix + ": " + func.__name__ + " -> " + repr(func(*args, **kwargs)))
            return func(*args, **kwargs)
        return inner
    return decorator


def module_test(mod):

    """Run all the test functions in the module mod (which is a module object).

    A test function is a function with a name that begins with "test".
    All the test functions take no arguments and throw an exception if
    the test fails.

    For each test, print a block to stderr in the following format:
      {test function name}: {either PASS or FAIL: {exception type name} {exception as a string}}
      {test function doc string}
    For example of a test is defined:
      def testA():
        '''Test A'''
        raise RuntimeError("Blah")
    Your function should print:
      testA: FAIL: RuntimeError 'Blah'
      Test A
    
    Make sure you handle functions without doc strings without crashing
    (you can treat it as an empty doc string).
    """
    func_list = [item[1] for item in mod.__dict__.items() if isinstance(item[0],str) and item[0].startswith('test')]    
    sys.stderr.write("\n".join([func.__name__ + ": " + ("PASS" if func() else "FAIL") for func in func_list] + [ func.__doc__ for func in func_list if func.__doc__ is not None]))
    sys.stderr.write("\n")
    
