from Foo import Foo


class FooImpl2(Foo):
    def __init__(self, param: str):
        self._param = param

    def param(self):
        return self._param + " and something extra from FooImpl2"
