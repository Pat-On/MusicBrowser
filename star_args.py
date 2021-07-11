# if you are using python 2
# from __future__ import print_function <- importing features of python 3 in python 2 !INTERESTING


print("Hello", "World", "Earth")


# *args is a tuple and it is going to unpack it so we can provide as many as we want
# because *args is going to unpack it
# from __future__ import division <- importing division to the python which is working like in P3

# so this astrix is doing magic
# convention is to use args like I was thinking the magic is doing *
# it has to appear as a last parameter
def average(arg1, arg2, *args):
    print(type(args))
    print("args is {}".format(args))
    print("*args is:", *args)  # so this with star is unpacking nice something like ... in js
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)  # in python 2 it is going to do integer division


print(average(1, 2, 3, 4))


#  challenge

def tuple_builder(*args):
    return args


print(tuple_builder(1, 2, 3, 4, 5))
