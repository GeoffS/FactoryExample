from foo_factories import simple_foo_factory
from foo_client import foo_client


if __name__ == "__main__":
    print("App1:")
    res = foo_client(simple_foo_factory)
    print(f'   foo_client result = "{res}"')