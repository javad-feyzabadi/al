
l = [1,2,3,4,5,6]
a = []
_marker = object()

def first(iterable,default=_marker):
    try:
        return next(iter(iterable))
    except StopIteration as e:
        if default is _marker:
            raise ValueError('first() was called on an emty iterable,'
                             'and no default value was provided') from e
        return default

