
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