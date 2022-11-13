from abc import ABC, abstractmethod

class Reader(ABC):
    def __init__(self, dataSource):
        self.dataSource = dataSource

    @abstractmethod
    def read(self):
        pass