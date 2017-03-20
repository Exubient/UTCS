"""Implement a class called TreeDict that supports operators the same
way as a dict. 

TreeDict should be implemented using the binarysearchtree module I
have provided (you can download it from canvas in the same folder as
this file).

You need to make sure you support the following operations with the
same semantics as a normal Python dict:
* td[key]
* td[key] = value
* key in td
* td.get(key)
* td.get(key, default)
* td.update(iterable_of_pairs_or_dict_or_TreeDict)
* len(td)
* for key in td: pass
* for key, value in td.items(): pass
* A constructor: TreeDict(iterable_of_pairs_or_dict_or_TreeDict)

Iteration should be in key order, this should be pretty easy to do
just by traversing the tree using an in-order traversal. None of the
iterator methods should make a copy of any of the data in the
TreeDict. You should only implement in-order traversal once and use
that implementation for both kinds of traversal.

You should support a constructor which takes the same arguments as
update and creates a TreeDict with just those values. There is an easy
way to do this in just a couple of lines using your existing update
method.

For each operation, make sure it does the same thing as a dict and you
handle errors by throwing the same type of exception as would be thrown
by a dict. However unlike dict your implementation will not support
None as a key and you should throw an appropriate exception if None is
used as a key. Look at the available built in exceptions and pick the
most appropriate one you find.

Most of these methods will be very short (just a couple of lines of
code), a couple will be a bit more complicated. However all the hard
work should already be handled by the binarysearchtree module. It
looks like a lot of operations, but it shouldn't actually take that
long. Many of the operations are quite similar as well.

Do not reimplement anything in the binarysearchtree module or copy
code from it. You should not need to.

For this assignment I expect you will have to use at least the
following things you have learned:
* Raising exceptions
* Catching exceptions
* Implementing magic methods
* Generators using yield (and you may want to look up "yield from")
* Type checks
* Default values/optional arguments

You will also need to read code which I think will help you learn to
think in and use Python.

To reiterate some of the things you should be aware of to avoid losing
points:
* None of the iterator methods should make a copy of any of the data
  in the TreeDict.
* You should only implement in-order traversal once and it should be
  recursive (it's so much easier that way).
* Do not reimplement anything in the binarysearchtree module or copy
  code from it.
* There are easy ways to implement all the required operations. If
  your implementation of a method is long you may want to think if
  there is a simpler way.

Links:
* https://docs.python.org/3.5/library/stdtypes.html#dict
* http://en.wikipedia.org/wiki/Binary_search_tree#Traversal
* https://docs.python.org/3.5/reference/expressions.html#yieldexpr

"""
# hk23356
# Hyun Joong Kim
from binarysearchtree import Node

class TreeDict(object):

    def __init__(self, *arg, **kwarg):
        self.node = Node()
        self.update(*arg, **kwarg)

    def __getitem__(self, key):
        if key is None:
            raise KeyError("None cannot be used as a key")
        try:
            return self.node.lookup(key).value
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key is None:
            raise KeyError("None cannot be used as a key")
        try:
            return self.node.insert(key, value)
        except ValueError:
            raise ValueError()

    def __contains__(self, key):
        if key is None:
            raise KeyError("None cannot be used as a key")
        try:
            if self.node.lookup(key).value != None:
                return True
        except ValueError:
            raise ValueError()

    def update(self, *arg, **kwarg):
        for key, value in kwarg.items():
            if key is None:
                raise KeyError("None cannot be used as a key")
            else:
                self.node.insert(key, value)
        if len(arg) != 0:
            if type(arg[0]).__name__ == "TreeDict":
                for node in arg[0]:
                    self.node.insert(node, arg[0][node])
            elif isinstance(arg[0], dict):
                for key, value in arg[0].items():
                    if key is None:
                        raise KeyError("None cannot be used as a key")
                    else:
                        self.node.insert(key, value)
            elif hasattr(arg[0], '__iter__'):
                for iter_element in arg[0]:
                    if len(iter_element) != 2:
                        raise ValueError(iter_element)
                    else:
                        if iter_element[0] == None:
                            raise ValueError(iter_element)
                        else:
                            self.node.insert(iter_element[0], iter_element[1])
            else:
                raise ValueError()

    def get(self, key, default=None):
        if key is None:
            raise KeyError("None cannot be used as a key")
        try:
            return self.node.lookup(key).value
        except ValueError:
            return default

    def num_subtree_Nodes(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.num_subtree_Nodes(root.left) + self.num_subtree_Nodes(root.right)

    def __len__(self):
        if self.node.key is None:
            return 0
        else:
            return self.num_subtree_Nodes(self.node.left) + self.num_subtree_Nodes(self.node.right) + 1

    def iterOrder(self, root):
        if root != None:
            yield from self.iterOrder(root.left)
            yield (root.key, root.value)
            yield from self.iterOrder(root.right)

    def __iter__(self):
        if self.node.key is None:
            return iter(())
        else:
            return (item[0] for item in self.iterOrder(self.node))

    def items(self):
        if self.node.key is None:
            return iter({})
        else:
            return (item for item in self.iterOrder(self.node))

    def values(self):
        if self.node.key == None:
            return iter(())
        else:
            return (item[1] for item in self.iterOrder(self.node))
