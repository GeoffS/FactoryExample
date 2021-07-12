from foo_factories import foo3_factory
from FooImpl2 import FooImpl2
from foo_client import foo_client

if __name__ == "__main__":
    print("App4:")
    res = foo_client(lambda foo_param: FooImpl2(foo_param))

    # Static type checking errors not caught by pycharm
    # These are caught by mypy.
    res = foo_client(lambda: FooImpl2("foo_param"))
    res = foo_client(foo3_factory)

    print(f'   foo_client result = "{res}"')
