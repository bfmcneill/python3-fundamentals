from functools import wraps
from timeit import default_timer as timer


def timeit(func):
    """
    Modified from Python timit decorator
    https://gist.github.com/winogradoff/8ea1372676bdc6b3a59a86d79a0a5f64
    """
    @wraps(func)
    def timed(*args, **kw):        
        ts = timer()
        result = func(*args, **kw)
        te = timer()
        print("function time {} : {} sec".format(func.__name__, te - ts))
        return result
    return timed


def tags(tag_name):
    """
    Guide to python function decorators
    https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
    """
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@timeit
@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello {}".format(name)



print(get_text("Sam"))
