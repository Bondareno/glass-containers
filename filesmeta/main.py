from filesmeta.common_minion import CommonMinion
from filesmeta.img_minion import ImgMinion
from filesmeta.pdf_minion import PDFMinion
from filesmeta.doc_minion import DocMinion
from filesmeta.gru import Gru

gru = Gru()

common_minion = CommonMinion()
img_minion = ImgMinion()
pdf_minion = PDFMinion()
doc_minion = DocMinion()

gru.add_minion(common_minion)
gru.add_minion(img_minion)
gru.add_minion(pdf_minion)
gru.add_minion(doc_minion)

file_paths = [...]  # Список путей к файлам, которые вы хотите обработать
metadata = [gru.get_meta_info(file_path) for file_path in file_paths]

# Теперь у вас есть метаинформация о каждом файле, которую вы можете использовать для создания CSV-файла или других операций.
