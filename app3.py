from foo_factories import foo2_factory
from foo_client import foo_client


if __name__ == "__main__":
    print("App3:")
    res = foo_client(foo2_factory)
    print(f'   foo_client result = "{res}"')