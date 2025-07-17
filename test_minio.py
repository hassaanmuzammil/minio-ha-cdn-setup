from minio import Minio
from time import time

client = Minio(
    endpoint="localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False,
)
bucket_name = "test-private"
object_name = "v1.mov"
file_path = "ignore/file.mov"

t1 = time()
url = client.get_presigned_url(
    method="GET",
    bucket_name=bucket_name,
    object_name=object_name,
)
# client.fget_object(
#     bucket_name=bucket_name,
#     object_name=object_name,
#     file_path=file_path,
# )
t2 = time()
print(f"Time Elapsed: {t2-t1} seconds\nURL: {url}")