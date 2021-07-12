from Foo import Foo
from FooImpl import FooImpl
from FooImpl2 import FooImpl2


def simple_foo_factory(foo_param: str) -> Foo:
    return FooImpl(foo_param)


def second_foo_factory(foo_param: str) -> Foo:
    return FooImpl(foo_param + " and something extra from the second_foo_factory")


def foo2_factory(foo_param: str) -> Foo:
    return FooImpl2(foo_param)


def foo3_factory() -> Foo:
    return FooImpl2("foo3_factory")
