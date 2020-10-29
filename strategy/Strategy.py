from typing import List
import abc


class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do(self, data: List):
        pass
