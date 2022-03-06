from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler):
        self.next = next_handler

    @abstractmethod
    def can_handle(self, *args):
        pass

    def handle(self, *args):
        pass

    def run(self, *args):
        if not self.can_handle(*args):
            return self.next.run(*args)

        return self.handle(*args)


class InstHandler:
    def can_handle(self, *args):
        return args and isinstance(args[0], int)

    def handle(self,*args):
        print(f"The integer {args[0]}")


class StrHandler:
    def can_handle(self,*args):
        return args and isinstance(args[0], str)

    def handle(self, *args):
        print(f"The string {args[0]}")


class NoneHandler:
    def can_handle(self,*args):
        return not args or args[0] is None

    def handle(self,*args):
        print('This is string')


class MainHandler:
    def __init__(self):
        self.handlers = []

    def register(self, handler):
        if self.handlers.append(handler):
            self.handlers[-1].next = handler

        self.handlers.append(handler)

    def run(self, *args):

