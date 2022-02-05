# Python_Extracting-Text-from-PDF-File
Extracting Text from PDF files.
# Extract text from PDF File using Python

All of you must be familiar with what PDFs are. In fact, they are one of the most important and widely used digital media. PDF stands for Portable Document Format. It uses .pdf extension. It is used to present and exchange documents reliably, independent of software, hardware, or operating system.

# Extracting Text from PDF File

Python package PyPDF can be used to achieve what we want (text extraction), although it can do more than what we need. This package can also be used to generate, decrypting and merging PDF files.

## Installation

To install this package type the below command in the terminal
```bash
pip install PyPDF2
```

## Usage

```python

# importing required modules 
import PyPDF2

# creating a pdf file object 
pdf_file = open("Manager Human Resources Job Description.pdf","rb")

# creating a pdf reader object 
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# printing number of pages in pdf file 
print(pdf_reader.numPages)

# extracting text from page 
print(pdf_reader.getPage(0).extractText())
```

## Reference
[GeekforGeeks](https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/)
