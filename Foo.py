from abc import ABC, abstractclassmethod, abstractmethod
from typing import Callable

class Foo(ABC):
    @abstractmethod
    def param(self) -> str: 
        pass