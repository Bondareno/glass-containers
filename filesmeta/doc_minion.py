from docx import Document
import os


class DocMinion:
    EX = {"doc", "docx"}

    def get_meta_info(self, path):
        metadata = {}
        try:
            if path.split(".")[-1].lower() in self.EX:
                doc = Document(path)
                paragraphs = [p.text for p in doc.paragraphs]
                author = doc.core_properties.author
                title = doc.core_properties.title
                created = doc.core_properties.created
                modified = doc.core_properties.modified

                metadata = {
                    "Paragraphs": paragraphs,
                    "Author": author,
                    "Title": title,
                    "Created Date": created,
                    "Modified Date": modified,
                }
            return metadata
        except Exception as e:
            return {"error": str(e)}
