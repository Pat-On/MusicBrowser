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

################# *KWARGS #################################

print("Hello World")


#  * unpacking tuple
#  ** unpacking dictionaries

# so we are passing by using **kwargs from the parameter to the our print()
#  and base on it we are unpacking the key-value pair and we can pass as many parameter as we want
# nice
# def print_backwards(*args,  **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=" ", **kwargs)

#          first solution to define end=" "
# def print_backwards(*args, end=" ", **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=" ", **kwargs)

# second solution is to remove "end" from the **kwargs
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=" ", **kwargs)


def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', "\n")
    sep_character = kwargs.pop('sep', " ")
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)  # and print the first word separately
    # print(end=end_character)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)  # list comprehension


with open("backwards.txt", 'w') as backwards:
    print(print_backwards("hello", "planet", "earth"))

# You can not specify two times the same argument <- two ways to fix it
with open("backwards.txt", 'w') as backwards:
    print(print_backwards("hello", "planet", "earth", file=backwards, end="\n"))
    print("Another String")

print("*" * 40)
print("hello", "planet", "earth", end="", sep="\n**\n")

print_backwards("hello", "planet", "earth", end="\n", sep="\n**\n")
print("=" * 40)
