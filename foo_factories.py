from FooImpl import FooImpl
from Foo import Foo


def simple_foo_factory(foo_param: str) -> Foo:
    return FooImpl(foo_param)


def second_foo_factory(foo_param: str) -> Foo:
    return FooImpl(foo_param+" and something extra from the second_foo_factory")