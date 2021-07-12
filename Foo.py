from abc import ABC, abstractmethod


class Foo(ABC):
    @abstractmethod
    def param(self) -> str:
        pass
