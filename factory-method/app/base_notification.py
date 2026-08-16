from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass

    @abstractmethod
    def validateRecipient(self, recipient: str) -> bool:
        pass