from abc import ABC, abstractmethod

class SignedUrlGenerator(ABC):

    @abstractmethod
    def generate_upload_url(self, upload_request: dict) -> str:
        pass

    @abstractmethod
    def generate_download_url(self, document_id: str) -> str:
        pass