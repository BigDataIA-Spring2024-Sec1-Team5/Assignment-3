# Define the URLClass model using Pydantic's BaseModel
from pydantic import BaseModel, Field, HttpUrl, ValidationError, validator
import pandas as pd  # For handling CSV file operations
import re  # Regular expressions library for text matching


class URLClass(BaseModel):
    # Define fields with types 
    # Aliases are used to match the CSV column names
    article: str = Field(alias='Article')
    topic: str = Field(alias='Topic')
    year: int = Field(alias='Year')
    level: str = Field(alias='Level')
    introduction: str = Field(alias='Introduction')
    learning_outcomes: str = Field(alias='Learning Outcomes')
    summary: str = Field(alias='Summary')
    link_to_the_summary_page: HttpUrl = Field(alias='Link to the Summary Page')
    link_to_the_pdf_file: HttpUrl = Field(alias='Link to the PDF File')

    # Validator to ensure certain text fields are not empty or just whitespace
    @validator('article', 'introduction', 'topic', 'learning_outcomes', 'summary', pre=True)
    def check_non_empty(cls, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("This field cannot be empty or just whitespace.")
        return v.strip()

#     # Validator to extract and validate the year from a string
#     @validator('year', pre=True)
#     def extract_year_and_format(cls, v):
#         year_match = re.search(r'\d{4}', v)
#         if year_match:
#             return int(year_match.group(0))
#         raise ValueError('Year must be a four-digit number and present in the field.')
    @validator('year', pre=True)
    def extract_year_and_format(cls, v):
         if isinstance(v, str):
            year_match = re.search(r'\d{4}', v)
            if year_match:
                return int(year_match.group(0))
            return "Year Not Found"

    # Validator to ensure the 'level' field does not start with "CFA Program"
    @validator('level', pre=True)
    def format_level(cls, v):
        clean_level = " ".join(v.split())
        if clean_level.startswith("CFA Program"):
            return "Level Not Found"  # Set to a default value if it starts with "CFA Program"
        return clean_level

 # Validator for the PDF link, ensuring it starts with "https://" or fixes relative URLs
    @validator('link_to_the_pdf_file', pre=True)
    def adjust_pdf_link(cls, v):
        if v.startswith('/'):
            return f"https://www.cfainstitute.org{v}"
        return v

    # Validator for the summary page link, ensuring it's a valid URL
    @validator('link_to_the_summary_page', pre=True)
    def validate_summary_link(cls, v):
        if not v.startswith('http'):
            raise ValueError('Summary page link must start with http or https.')
        return v


import pytest
 # Adjust the import based on your project's structure

# Define test data for passing scenarios
@pytest.mark.parametrize("data", [
    # Valid Complete Data
    {"Article": "Valid Article", "Topic": "Valid Topic", "Year": "2024", "Level": "Level II", 
     "Introduction": "This is a valid introduction.", "Learning Outcomes": "Learner will understand X, Y, Z.", 
     "Summary": "In summary, X leads to Y.", "Link to the Summary Page": "example.com/summary", 
     "Link to the PDF File": "https://example.com/pdf/file.pdf"},
    # Year as String with Correct Format
    {"Article": "Year Extraction", "Topic": "Year Test", "Year": "Published in 2024", "Level": "Level I", 
     "Introduction": "Year extraction from string.", "Learning Outcomes": "Understand year extraction.", 
     "Summary": "Year was extracted.", "Link to the Summary Page": "http://example.com/year-extraction", 
     "Link to the PDF File": "/pdf/year-extraction.pdf"},
    # Level Field Without 'CFA Program' Prefix
    {"Article": "Level Formatting", "Topic": "Level Test", "Year": "2024", "Level": "Level II", 
     "Introduction": "Level formatting test.", "Learning Outcomes": "Understand level formatting.", 
     "Summary": "Level formatted.", "Link to the Summary Page": "http://example.com/level-formatting", 
     "Link to the PDF File": "https://example.com/pdf/level-formatting.pdf"},
    # PDF Link Starts with '/'
    {"Article": "PDF Link Adjustment", "Topic": "PDF Link Test", "Year": "2024", "Level": "Level II", 
     "Introduction": "PDF link adjustment test.", "Learning Outcomes": "Understand PDF link adjustment.", 
     "Summary": "PDF link adjusted.", "Link to the Summary Page": "http://example.com/pdf-link-adjustment", 
     "Link to the PDF File": "/pdf/pdf-link-adjustment.pdf"},
    # Summary Page Link with HTTP
    {"Article": "Valid HTTP Summary Link", "Topic": "HTTP Link Test", "Year": "2024", "Level": "Level I", 
     "Introduction": "HTTP summary link test.", "Learning Outcomes": "Understand HTTP summary link.", 
     "Summary": "HTTP summary link valid.", "Link to the Summary Page": "http://example.com/http-summary-link", 
     "Link to the PDF File": "https://example.com/pdf/http-summary-link.pdf"}
])
def test_url_class_valid(data):
    # This should not raise a ValidationError
    URLClass(**data)

# Define test data for failing scenarios
@pytest.mark.parametrize("data, expected_error", [
    # Empty Article Field
    ({"Article": "", "Topic": "Invalid Topic", "Year": "2024", "Level": "Level II", 
      "Introduction": "Invalid due to empty article.", "Learning Outcomes": "None due to error.", 
      "Summary": "Empty article error.", "Link to the Summary Page": "http://example.com/empty-article", 
      "Link to the PDF File": "https://example.com/pdf/empty-article.pdf"}, "article"),
    # Invalid Year Format (String Without Year)
    ({"Article": "Invalid Year Format", "Topic": "Year Format Test", "Year": "No Year", "Level": "Level I", 
      "Introduction": "Year format test.", "Learning Outcomes": "Understand year format failure.", 
      "Summary": "Year format failed.", "Link to the Summary Page": "http://example.com/year-format-fail", 
      "Link to the PDF File": "https://example.com/pdf/year-format-fail.pdf"}, "year"),
    # Level Field Starts with 'CFA Program'
    ({"Article": "Invalid Level Prefix", "Topic": "Level Prefix Test", "Year": "2024", "Level": "CFA Program Level II", 
      "Introduction": "Level prefix test.", "Learning Outcomes": "Understand level prefix failure.", 
      "Summary": "Level prefix failed.", "Link to the Summary Page": "http://example.com/level-prefix-fail", 
      "Link to the PDF File": "https://example.com/pdf/level-prefix-fail.pdf"}, "level"),
    # Invalid PDF Link (Missing HTTPS)
    ({"Article": "Invalid PDF Link", "Topic": "PDF Link Test", "Year": "2024", "Level": "Level II", 
      "Introduction": "PDF link test.", "Learning Outcomes": "Understand PDF link failure.", 
      "Summary": "PDF link failed.", "Link to the Summary Page": "http://example.com/pdf-link-fail", 
      "Link to the PDF File": "example.com/pdf/pdf-link-fail.pdf"}, "link_to_the_pdf_file"),
    # Invalid Summary Page Link (Missing HTTP/HTTPS)
    ({"Article": "Invalid Summary Link", "Topic": "Summary Link Test", "Year": "2024", "Level": "Level I", 
      "Introduction": "Summary link test.", "Learning Outcomes": "Understand summary link failure.", 
      "Summary": "Summary link failed.", "Link to the Summary Page": "example.com/summary-link-fail", 
      "Link to the PDF File": "https://example.com/pdf/summary-link-fail.pdf"}, "link_to_the_summary_page")
])
def test_url_class_invalid(data, expected_error):
    with pytest.raises(ValidationError) as exc_info:
        URLClass(**data)
    assert expected_error in str(exc_info.value)
