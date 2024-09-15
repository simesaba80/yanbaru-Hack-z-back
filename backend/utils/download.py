from fastapi import HTTPException
from google.cloud import storage


def download_blob(bucket_name: str, source_blob_name: str, destination_file_name: str):
    """Google Cloud Storageからファイルをダウンロードする"""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
        return destination_file_name
    except Exception as e:
        print(f"Error downloading blob: {e}")
        raise HTTPException(status_code=500, detail="Error downloading file")
