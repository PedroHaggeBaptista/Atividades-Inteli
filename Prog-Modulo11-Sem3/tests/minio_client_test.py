# Faça os testes para os métodos create_bucket_if_not_exists, upload_file e download_file do módulo aulaafonse/minio_client.py.

from aulaafonse.minio_client import create_bucket_if_not_exists, upload_file, download_file
import os
import pytest

def test_create_bucket_if_not_exists():
    bucket_name = "test-bucket"
    create_bucket_if_not_exists(bucket_name)
    assert True

def test_upload_file():
    bucket_name = "test-bucket"
    file_path = "test.txt"
    with open(file_path, "w") as file:
        file.write("Este é um arquivo de teste.")
    
    upload_file(bucket_name, file_path)
    assert True

def test_download_file():
    bucket_name = "test-bucket"
    file_name = "test.txt"
    local_file_path = f"downloaded_{file_name}"
    download_file(bucket_name, file_name, local_file_path)

    with open(local_file_path, "r") as file:
        downloaded_content = file.read()
        assert downloaded_content == "Este é um arquivo de teste."
    
    os.remove(file_name)
    os.remove(local_file_path)