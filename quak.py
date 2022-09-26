# **kwargs: passing Dictionaries #
""" https://www.data-science-architect.de/args-kwargs/ """


# No **kwargs
def no_kwargs(a):
    return print(a)


myDict1 = {'b': 2, 'a': 1, 'c': 3}
no_kwargs(myDict1)


# With **kwargs
def with_kwargs(a, b, c, **kwargs):
    """ a, b, c representing the keys inside the Dictionary """
    return print(a, b, c, **kwargs)


myDict2 = {'b': 2, 'a': 1, 'c': 3}
with_kwargs(**myDict2)


# Error with **kwargs
# def with_kwargs(a, b, c, **kwargs):
#     """ a, b, c representing the keys inside the Dictionary """
#     return print(a, b, c, **kwargs)  # error, invalid keyword: d is missing from the Dictionary
#
#
# myDict3 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
# with_kwargs(**myDict3)


# prevent error with **kwargs
def with_kwargs(a, b, c, d, **kwargs):  # same keys needed as the Dictionary provides
    """ a, b, c representing the keys inside the Dictionary """
    return print(d, a, c)  # but return, whatever you want


myDict3 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
with_kwargs(**myDict3)
