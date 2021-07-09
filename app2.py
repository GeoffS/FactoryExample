from foo_factories import second_foo_factory
from foo_client import foo_client


if __name__ == "__main__":
    print("App2:")
    res = foo_client(second_foo_factory)
    print(f'   foo_client result = "{res}"')