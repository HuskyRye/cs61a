""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    while link.rest != Link.empty:
        if link.rest.first == value:
            link.rest = link.rest.rest
        else:
            link = link.rest

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    while link != Link.empty:
        if isinstance(link.first, int):
            link.first = fn(link.first)
        else:
            deep_map_mut(fn, link.first)
        link = link.rest

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    has_seen = list()
    while link != Link.empty:
        if link in has_seen:
            return True
        else:
            has_seen.append(link)
        link = link.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    >>> u = Link(1, Link(2, Link(3)))
    >>> u.rest.rest.rest = u.rest
    >>> has_cycle_constant(u)
    True
    """

    '''
    # Wrong
    mark = link
    while link != Link.empty:
        link = link.rest
        if mark is link:
            return True
    return False
    '''
    slow = link
    fast = link.rest
    while slow != Link.empty and fast != Link.empty:
        if slow == fast:
            return True
        slow = slow.rest
        fast = fast.rest.rest
    return False

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    labels = [branch.label for branch in t.branches]
    labels.reverse()
    for index, branch in enumerate(t.branches):
        branch.label = labels[index]
    
    for branch in t.branches:
        for branch_of_branches in branch.branches:
            reverse_other(branch_of_branches)
    