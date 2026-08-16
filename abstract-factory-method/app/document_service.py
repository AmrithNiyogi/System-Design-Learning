from app.factory import CloudStorageFactory


class DocumentService:

    def __init__(self, factory: CloudStorageFactory):
        self._storage_client = factory.create_storage_client()
        self._signed_url_generator = factory.create_signed_url_generator()
        self._metadata_repository = factory.create_metadata_repository()

    def upload_document(self, upload_request: dict) -> dict:
        self._storage_client.validate_upload(upload_request)
        upload_url = self._signed_url_generator.generate_upload_url(upload_request)
        document_id = upload_request.get("document_id") or upload_request["filename"]
        metadata = {
            **upload_request,
            "document_id": document_id,
        }
        self._metadata_repository.save(metadata)
        return {
            "document_id": document_id,
            "upload_url": upload_url,
        }

    def download_document(self, document_id: str) -> dict:
        metadata = self._metadata_repository.get(document_id)
        download_url = self._signed_url_generator.generate_download_url(document_id)
        return {
            "document_id": document_id,
            "download_url": download_url,
            "metadata": metadata,
        }
