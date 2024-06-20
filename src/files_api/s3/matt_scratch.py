import os

import boto3

from files_api.s3.write_objects import upload_s3_object

BUCKET_NAME = "python-course-matt-aws--test-bucket-6-19-24"


def main():
    s3_client = boto3.client("s3")
    file_content = b"test content from matt scratch"
    upload_s3_object(
        BUCKET_NAME,
        "testfile.txt",
        file_content,
        content_type="text/plain",
        s3_client=s3_client,
    )
    # response = s3_client.get_object(Bucket=BUCKET_NAME, Key="testfile.txt")
    # assert response["Body"].read() == file_content


if __name__ == "__main__":
    main()
