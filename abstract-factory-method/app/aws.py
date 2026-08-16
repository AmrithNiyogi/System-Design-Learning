from app.storage_client import StorageClient
from app.signed_url_generator import SignedUrlGenerator
from app.metadata_repository import MetadataRepository


class S3StorageClient(StorageClient):
    
    def validate_upload(self, upload_request: dict) -> None:
        if not upload_request.get("filename"):
            raise ValueError("Filename is required")


class S3SignedUrlGenerator(SignedUrlGenerator):

    def generate_upload_url(self, upload_request: dict) -> str:
        filename = upload_request["filename"]
        return f"https://s3.amazonaws.com/docs/{filename}?upload=1"

    def generate_download_url(self, document_id: str) -> str:
        return f"https://s3.amazonaws.com/docs/{document_id}?download=1"


class DynamoMetadataRepository(MetadataRepository):

    def __init__(self):
        self._store = {}


    def save(self, metadata: dict) -> None:
        self._store[metadata["document_id"]] = metadata


    def get(self, document_id: str) -> dict:
        return self._store.get(document_id)