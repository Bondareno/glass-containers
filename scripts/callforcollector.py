from utils import files

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
