from Foo import Foo

class FooImpl(Foo):
    def __init__(self, param: str):
        self._param = param

    def param(self): 
        return self._param