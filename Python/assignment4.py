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
    raise NotImplementedError

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
    raise NotImplementedError
    
