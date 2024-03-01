from pydantic import BaseModel, HttpUrl, validator, ValidationError, HttpUrl
from datetime import datetime

class MetaDataPDFClass(BaseModel):
    level: str
    file_size_kb: float  # File size in KB
    amazon_storage_class: str
    s3_text_link: HttpUrl  # S3 link to the PDF
    file_path: str
    content_type: str = "txt"  # Default content type as text
    date_updated: datetime

    # Validator for Amazon Storage Class
    @validator('amazon_storage_class')
    def storage_class_must_be_standard_or_glacier(cls, v):
        if v not in ["Standard", "Glacier"]:
            raise ValueError('Amazon_storage_class must be "Standard" or "Glacier"')
        return v

    # Validator for file size to ensure it's positive
    @validator('file_size_kb')
    def file_size_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('file_size_kb must be a positive number')
        return v

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
