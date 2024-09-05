from abc import ABC, abstractmethod


# ABC means abstract class

class InvalidOperationError(Exception):
    pass


# (ABC) to define Stream class as abstract class
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed")
        self.opened = False

    # abstract method define
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")
