from minio import Minio
from backend.core.config import settings
import io, os
import datetime as dt

# https://github.com/minio/minio-py/blob/master/examples/get_object.py

minio_client = Minio(f"{settings.MINIO_ENDPOINT}:{settings.MINIO_PORT}",access_key=f"{settings.MINIO_ACCESS_KEY}", secret_key=f"{settings.MINIO_SECRET_KEY}", secure=False)

def put_object(bucket_name, file):

    try:
        contents = file.file.read()
        temp_file = io.BytesIO()
        temp_file.write(contents)
        temp_file.seek(0)

        found = minio_client.bucket_exists(bucket_name)
        if not found:
            minio_client.make_bucket(bucket_name)
            print("Created bucket", bucket_name)
        else:
            print("Bucket", bucket_name, "already exists")
        
        file_size = os.fstat(file.file.fileno()).st_size
        _object_name=f"{dt.datetime.now().timestamp()}.{os.path.splitext(file.filename)[1][1:].strip()}"
        data=minio_client.put_object(bucket_name, _object_name, temp_file, file_size)
        temp_file.close()
        
        return data
    
    except Exception as e:
        print(f"Error function put_object: {e}")
        return None
    
def get_object(bucket_name, filename):
    try:
        response = minio_client.get_object(
        bucket_name, filename
        )
        return response
    except Exception as e:
        print(f"Error function get_object: {e}")
        return None
    
