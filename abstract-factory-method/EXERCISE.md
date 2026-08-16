**Scenario:** Build a multi-cloud object-storage service for a document-management platform. The system initially stores documents in AWS S3, but now must support Google Cloud Storage and Azure Blob Storage. Each cloud provider requires its own compatible storage client, signed-URL generator, and metadata store.

### Requirements
- Support `AWS`, `GCP`, and `Azure` storage providers.
- Every provider must supply a compatible family of services:
  - `StorageClient`
  - `SignedUrlGenerator`
  - `MetadataRepository`
- The document workflow must:
  1. Validate a file upload request
  2. Generate an upload URL
  3. Store document metadata
  4. Generate a download URL when requested
- The workflow must **not** depend directly on `S3StorageClient`, `GCSStorageClient`, or `AzureBlobStorageClient`.
- Services produced for one provider must not be mixed with another provider’s services.
- Adding a new provider later should require new classes, not changes to the document workflow.
- Assume provider credentials and configuration are supplied at application startup.

### Your Task
Design the classes and interactions in Python using the **Abstract Factory** pattern.

Include:
- Product abstractions:
  - `StorageClient`
  - `SignedUrlGenerator`
  - `MetadataRepository`
- Concrete product families:
  - `S3StorageClient`, `S3SignedUrlGenerator`, `DynamoMetadataRepository`
  - `GCSStorageClient`, `GCSSignedUrlGenerator`, `FirestoreMetadataRepository`
  - `AzureBlobStorageClient`, `AzureSignedUrlGenerator`, `CosmosMetadataRepository`
- A `CloudStorageFactory` abstraction that defines:
  - `create_storage_client()`
  - `create_signed_url_generator()`
  - `create_metadata_repository()`
- Concrete factories for AWS, GCP, and Azure.
- A `DocumentService` that receives a `CloudStorageFactory`.
- Application bootstrap code that chooses a factory using application configuration.

### Expected Outcome
Your Python design should allow this:

```python
service = DocumentService(AWSStorageFactory(config))
service.upload_document(upload_request)

service = DocumentService(GCPStorageFactory(config))
service.upload_document(upload_request)
```

Each service executes the same document workflow while using a compatible cloud-provider-specific service family.

### Constraints
- Do not put a growing `if provider == ...` block inside `DocumentService`.
- Do not instantiate concrete cloud-provider classes in document workflow code.
- Keep credentials inside provider-specific construction/configuration.
- Keep the design open for a new cloud provider without modifying `DocumentService`.

### Discussion Prompts
1. Why does this require Abstract Factory instead of Factory Method?
2. How do you prevent accidental mixing of AWS and GCP service objects?
3. How would you test `DocumentService` without real cloud credentials?
4. When would dependency injection with prebuilt clients be simpler than Abstract Factory?
