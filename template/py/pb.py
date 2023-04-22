from functools import wraps
from random import uniform
from time import sleep
from time import time_ns

# f = dec(*, max=3.0)(f)
def fake_payload(*, max=3.0):
    def add_sleep(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(uniform(0.0, max))
            return func(*args, **kwargs)

        return wrapper

    return add_sleep
