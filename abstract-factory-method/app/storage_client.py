from abc import ABC, abstractmethod

class StorageClient(ABC):

    @abstractmethod
    def validate_upload(self, upload_request: dict) -> None:
        pass