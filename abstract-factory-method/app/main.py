
import argparse
from app.document_service import DocumentService
from app.factory import (
    AWSStorageFactory,
    GCPStorageFactory,
    AzureStorageFactory,
)

FACTORIES = {
    "aws": AWSStorageFactory(),
    "gcp": GCPStorageFactory(),
    "azure": AzureStorageFactory(),
}

def parse_args():
    parser = argparse.ArgumentParser(description="Upload a document via a cloud provider.")
    parser.add_argument(
        "--provider",
        default="aws",
        help="Cloud provider: aws, gcp, or azure (default: aws)"
    )

    return parser.parse_args()

def main():
    args = parse_args()

    if args.provider not in FACTORIES:
        raise ValueError(f"Invalid provider: {args.provider}")

    factory = FACTORIES[args.provider]
    service = DocumentService(factory)

    upload_request = {
        "filename": "example.pdf",
        "content": "This is a test document.",
        "document_id": "docu-1",
    }

    print(f"Uploaded document: {service.upload_document(upload_request)}")
    print(f"Downloaded document: {service.download_document('docu-1')}")

if __name__ == "__main__":
    main()