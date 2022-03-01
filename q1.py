import function

def safe_call(f: function, **kwargs):
    for key, value in kwargs.items():
        if key in f.__annotations__:
            key_type = f.__annotations__[key]
            if not isinstance(value, key_type):
                raise Exception('annotation not fit')
    return f(**kwargs)

def fun(x: int, y: float, z):
    return x + y + z


