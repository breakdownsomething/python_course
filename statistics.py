from collections import namedtuple
from collections import defaultdict

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])


def collect_statistics(statistics):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)


            # with open("test.txt", 'w') as f:
            #     f.write(str(result))
            return result
        return wrapped
    return decorator
