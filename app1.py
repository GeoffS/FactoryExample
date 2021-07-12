from foo_client import foo_client
from foo_factories import simple_foo_factory

if __name__ == "__main__":
    print("App1:")
    res = foo_client(simple_foo_factory)
    print(f'   foo_client result = "{res}"')
