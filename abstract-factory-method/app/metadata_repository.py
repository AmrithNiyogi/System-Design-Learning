from abc import ABC, abstractmethod

class MetadataRepository(ABC):

    @abstractmethod
    def save(self, metadata: dict) -> None:
        pass


    @abstractmethod
    def get(self, document_id: str) -> dict:
        pass