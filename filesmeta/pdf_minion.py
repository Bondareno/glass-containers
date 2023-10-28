from PyPDF2 import PdfFileReader
import os


class PDFMinion:
    EX = {"pdf"}

    def get_meta_info(self, path):
        metadata = {}
        try:
            if path.split(".")[-1].lower() in self.EX:
                with open(path, 'rb') as pdf_file:
                    pdf_reader = PdfFileReader(pdf_file)
                    num_pages = pdf_reader.getNumPages()
                    author = pdf_reader.getDocumentInfo().author
                    creator = pdf_reader.getDocumentInfo().creator
                    producer = pdf_reader.getDocumentInfo().producer
                    subject = pdf_reader.getDocumentInfo().subject
                    title = pdf_reader.getDocumentInfo().title

                metadata = {
                    "Number of Pages": num_pages,
                    "Author": author,
                    "Creator": creator,
                    "Producer": producer,
                    "Subject": subject,
                    "Title": title,
                }
            return metadata
        except Exception as e:
            return {"error": str(e)}

