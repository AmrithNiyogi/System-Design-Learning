from abc import ABC, abstractmethod
from app.storage_client import StorageClient
from app.signed_url_generator import SignedUrlGenerator
from app.metadata_repository import MetadataRepository
from app.aws import (
    S3StorageClient, 
    S3SignedUrlGenerator, 
    DynamoMetadataRepository
    )
from app.gcp import (
    GCSStorageClient, 
    GCSSignedUrlGenerator, 
    FirestoreMetadataRepository
    )
from app.azure import (
    AzureBlobStorageClient, 
    AzureSignedUrlGenerator, 
    CosmosMetadataRepository
    )


class CloudStorageFactory(ABC):

    @abstractmethod
    def create_storage_client(self) -> StorageClient:
        pass


    @abstractmethod
    def create_signed_url_generator(self) -> SignedUrlGenerator:
        pass


    @abstractmethod
    def create_metadata_repository(self) -> MetadataRepository:
        pass


class AWSStorageFactory(CloudStorageFactory):

    def create_storage_client(self) -> StorageClient:
        return S3StorageClient()

    def create_signed_url_generator(self) -> SignedUrlGenerator:
        return S3SignedUrlGenerator()

    def create_metadata_repository(self) -> MetadataRepository:
        return DynamoMetadataRepository()


class GCPStorageFactory(CloudStorageFactory):

    def create_storage_client(self) -> StorageClient:
        return GCSStorageClient()

    def create_signed_url_generator(self) -> SignedUrlGenerator:
        return GCSSignedUrlGenerator()

    def create_metadata_repository(self) -> MetadataRepository:
        return FirestoreMetadataRepository()
        

class AzureStorageFactory(CloudStorageFactory):

    def create_storage_client(self) -> StorageClient:
        return AzureBlobStorageClient()

    def create_signed_url_generator(self) -> SignedUrlGenerator:
        return AzureSignedUrlGenerator()

    def create_metadata_repository(self) -> MetadataRepository:
        return CosmosMetadataRepository()