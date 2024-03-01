from pydantic import BaseModel, HttpUrl, validator, ValidationError, HttpUrl
from datetime import datetime

import pytest
from your_module import MetaDataPDFClass  # Replace 'your_module' with the name of your Python file where MetaDataPDFClass is defined.

import pytest
# Test cases that should pass
@pytest.mark.parametrize("data", [
    {"level": "I", "file_size_kb": 35.8, "amazon_storage_class": "Standard", "s3_text_link": "https://example.com/data1.txt", "file_path": "data/data1.txt", "date_updated": datetime(2024, 2, 27)},
    {"level": "II", "file_size_kb": 45.0, "amazon_storage_class": "Glacier", "s3_text_link": "https://example.com/data2.txt", "file_path": "data/data2.txt", "date_updated": datetime(2024, 2, 27)},
    {"level": "III", "file_size_kb": 30, "amazon_storage_class": "Standard", "s3_text_link": "https://example.com/data3.txt", "file_path": "data/data3.txt", "date_updated": datetime(2024, 2, 27)},
    {"level": "I", "file_size_kb": 60, "amazon_storage_class": "Standard", "s3_text_link": "https://example.com/data4.txt", "file_path": "data/data4.txt", "date_updated": datetime(2024, 2, 27)},
    {"level": "II", "file_size_kb": 50, "amazon_storage_class": "Glacier", "s3_text_link": "https://example.com/data5.txt", "file_path": "data/data5.txt", "date_updated": datetime(2024, 2, 27)}
])
def test_valid_metadata_pdf_class(data):
    assert MetaDataPDFClass(**data)

# Test cases that should fail
@pytest.mark.parametrize("data", [
    {"level": "I", "file_size_kb": -35.8, "amazon_storage_class": "Standard", "s3_text_link": "https://example.com/data1.txt", "file_path": "data/data1.txt", "date_updated": datetime(2024, 2, 27)},  # Negative file size
    {"level": "II", "file_size_kb": 45.0, "amazon_storage_class": "InvalidClass", "s3_text_link": "https://example.com/data2.txt", "file_path": "data/data2.txt", "date_updated": datetime(2024, 2, 27)},  # Invalid storage class
    {"level": "III", "file_size_kb": "thirty", "amazon_storage_class": "Standard", "s3_text_link": "https://example.com/data3.txt", "file_path": "data/data3.txt", "date_updated": datetime(2024, 2, 27)},  # Invalid file size type
    {"level": "I", "file_size_kb": 60, "amazon_storage_class": "Standard", "s3_text_link": "not_a_url", "file_path": "data/data4.txt", "date_updated": datetime(2024, 2, 27)},  # Invalid URL
    {"level": "II", "file_size_kb": 50, "amazon_storage_class": "Glacier", "s3_text_link": "https://example.com/data5.txt", "file_path": "data/data5.txt", "date_updated": "invalid_date"}  # Invalid date format
])
def test_invalid_metadata_pdf_class(data):
    with pytest.raises((ValidationError, ValueError, TypeError)):
        MetaDataPDFClass(**data)
