# Assignment-3

## Live application Links
[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1H02nPi64xmAH9DNvVs2ri15O0f36IX3hWvasRI22rFc#0)
[![workflow_architecture](https://img.shields.io/badge/workflow_architecture-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1U5TkNyjqhqrwY55DpaRgKcxTjDZOLemI#scrollTo=-Qt9Twsbjrjy)
[![Scraping](https://img.shields.io/badge/Sccraping-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1HKK_TbHFuo1RNRpOj3LEbVgWnz3oFUM7#scrollTo=GxxIHdiOov8D)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1xaizQ7Z6JdHKWwptp0O5qHPHVSbjCs7u#scrollTo=NGR0M3oaoWZK) <br>
[![Metadata_Grobid](https://img.shields.io/badge/Metadata_Grobid-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1udLCjcjwdSC0Wg05QLp6W7zboybkkWJR#scrollTo=WdjzuHj5oPEu)
[![Grobid_LXML](https://img.shields.io/badge/Grobid_LXML-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1uRJkYiCq61ihazmEVIuHuRkq-p3xQAJh)
[![Grobid_LXML](https://img.shields.io/badge/Grobid_LXML-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1uRJkYiCq61ihazmEVIuHuRkq-p3xQAJh)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1XsSpkZx7PLmYqxxIEICuHFReGapJBN_y#scrollTo=pUnnfr7tm-9I)
[![AWS S3](https://img.shields.io/badge/AWSS3-FC6600?style=for-the-badge&logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1g_Bk6w_gKwhdU6hZbQ9qSiA-Yo3UKr0P?usp=sharing)

## Problem Statement
*Data Modeling and Transformation with Python, Pydantic, and DBT*

## Project Goals
*The project aims to design, validate, and transform data using Python, Pydantic, and DBT. It involves creating Python classes to represent webpages and PDF files' schemas, enforcing guidelines for data consistency, and generating clean CSV files. By leveraging Pydantic, the data validation process ensures integrity and reliability. Test cases are developed to demonstrate successful validation and potential failure scenarios. Additionally, the project explores DBT and Snowflake for data transformation workflows. This includes loading clean data into Snowflake, creating summary tables using DBT, and materializing them for analysis. Tests are written to validate new table columns, and models are documented for clarity and future reference. Ultimately, the project establishes a test and production environment in Snowflake to facilitate seamless testing and deployment of DBT models.*

## Technologies Used
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Beautiful Soup](https://img.shields.io/badge/beautiful_soup-109989?style=for-the-badge&logo=beautiful_soup&logoColor=white)](https://pypi.org/project/beautifulsoup4/)
[![Selenium](https://img.shields.io/badge/Selenium-39e75f?style=for-the-badge&logo=selenium&logoColor=blue)](https://www.selenium.dev/)
[![Grobid](https://img.shields.io/badge/grobid-909090?style=for-the-badge&logo=grobid&logoColor=blue)](https://grobid.readthedocs.io/en/latest/Introduction/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-123499?style=for-the-badge&logo=python&logoColor=blue)](https://pypi.org/project/PyPDF2/)
[![Snowflake](https://img.shields.io/badge/Snowflake-90e0ef?style=for-the-badge&logo=snowflake&logoColor=blue)](https://www.snowflake.com/en/)
[![Amazon S3](https://img.shields.io/badge/Amazon_S3-FF4B4B?style=for-the-badge&logo=Amazon_S3&logoColor=white)](https://aws.amazon.com/s3/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

## Data Sources
*The data source is the [CFA Institute's Refresher Readings](https://www.cfainstitute.org/membership/professional-development/refresher-readings/#sort=%40refreadingcurriculumyear%20descending)* and the provided PDF files.

## Architecture Workflow
![CFA_Extraction](https://github.com/BigDataIA-Spring2024-Sec1-Team5/Assignment2/assets/114545333/93cb5f1c-d4c5-42ac-be78-ace7a1e334b4)

## Pre requisites
*Installed Libraries of Python, Beautiful Soup, Selenium, PyPDF2, lxml eTree, Snowflake, SQLAlchemy*

## Project Structure
```
📦 Assignment2
├─ ReadME
|- Notebooks
│  ├─ Scrapping.ipynb
│  ├─ PyPDF2_Team05.ipynb
│  ├─ grobid_script.sh
│  ├─ grobid_lxml_team05.ipynb
│  ├─ metadata_structured_code.ipynb
│  ├─ snowflake_requirements.txt
│  ├─ AWS_S3.py
│  ├─ Grobid_Snowflake.py
│  └─ SQLAlchemy.py
├─ Outputs
│  ├─ Team05.csv
│  ├─ Metadata
│  │  ├─ json
│  │  │  ├─ 2024-l1-topics-combined-structured-metadata.json
│  │  │  ├─ 2024-l2-topics-combined-structured-metadata.json
│  │  │  └─ 2024-l3-topics-combined-structured-metadata.json
│  │  └─ csv
│  │     ├─ 2024-l1-topics-combined-structured-metadata.csv
│  │     ├─ 2024-l2-topics-combined-structured-metadata.csv
│  │     └─ 2024-l3-topics-combined-structured-metadata.csv
│  ├─ grobid_xml_files
│  │  ├─ Grobid_RR_2024_LevelIII_combined.xml
│  │  ├─ Grobid_RR_2024_LevelII_combined.xml
│  │  └─ Grobid_RR_2024_LevelI_combined.xml
│  ├─ grobid_text_files
│  │  ├─ Grobid_RR_2024_LevelIII_combined.txt
│  │  ├─ Grobid_RR_2024_LevelII_combined.txt
│  │  └─ Grobid_RR_2024_LevelI_combined.txt
│  └─ pypdf_extracted_texts
│     ├─ PyPDF_2024_l1_combined.txt.txt
│     ├─ PyPDF_2024_l2_combined.txt
│     └─ PyPDF_2024_l3_combined.tx
├─ PDF Files
│  ├─ 2024-l1-topics-combined-2.pdf
│  ├─ 2024-l2-topics-combined-2.pdf
│  └─ 2024-l1-topics-combined-2.pdf
└─ Images
   ├─ bs.png
   ├─ CFA.png
   ├─ CFA_Extraction.png
   ├─ csv.png
   ├─ grobid.png
   ├─ pdf.png
   ├─ pypdf2.png
   ├─ s3.png
   ├─ se.pn
   ├─ snow.png
   ├─ txt.png
   └─ xml.png
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## References
https://grobid.readthedocs.io/en/latest/Introduction/ <br>
https://www.sqlalchemy.org/ <br>
https://docs.snowflake.com/en/developer-guide/python-connector/sqlalchemy  <br>
https://pypdf2.readthedocs.io/en/3.0.0/ <br>
https://lxml.de/  <br>
https://aws.amazon.com/s3/   <br>
https://aws.amazon.com/iam/

## Learning Outcomes
* The objective of this assignment is to gain with comprehensive skills and practical experience in data modeling, validation, and transformation using Python, Pydantic, and DBT. Through the design of Python classes for schema representation, validation of data integrity with Pydantic, and exploration of web scraping and PDF processing techniques, will develop a robust foundation in data management. Test-driven development practices with Pytest and version control using Git will ensure code reliability and collaboration efficiency. Ultimately, learners will deploy DBT models seamlessly in test and production environments, enhancing critical thinking abilities to analyze complex data scenarios and propose innovative solutions. Effective documentation and communication skills will enable learners to articulate insights.This project will enhance the learning experience for finance professionals by providing an intelligent app interface to interact with curated finance materials*

## Team Information and Contribution 

Name | Contribution %| Contributions |
--- |--- | --- |
Aditya Kanala | 33% | Web Scrapping|
Shubh Patel | 34% | Extraction using Pypdf2 and Grobid |
Shikhar Patel | 33% | Snowflake using SQLAlchemy and Amazon S3 |
