#from utils import files
import sys

from filesmeta.common_minion import CommonMinion
from filesmeta.doc_minion import DocMinion
from filesmeta.gru import Gru
from filesmeta.img_minion import ImgMinion
from filesmeta.pdf_minion import PDFMinion
from collector import Collector

if __name__ == "__main__":
    directory = "/Users/ekaterinabondarenko"
    sqlite_path = "/путь/к/вашей/базе.sqlite"

    g = Gru()
    m1 = ImgMinion()
    m2 = PDFMinion()
    m3 = DocMinion()
    m4 = CommonMinion()
    g.add_minion(m1)
    g.add_minion(m2)
    g.add_minion(m3)
    g.add_minion(m4)

    c = Collector(g, directory, sqlite_path)
    c.collect()
