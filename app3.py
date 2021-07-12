from foo_client import foo_client
from foo_factories import foo2_factory

if __name__ == "__main__":
    print("App3:")
    res = foo_client(foo2_factory)
    print(f'   foo_client result = "{res}"')
