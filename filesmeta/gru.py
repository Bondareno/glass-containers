class Gru:
    def __init__(self):
        self.minions = []

    def add_minion(self, minion):
        self.minions.append(minion)

    def gru_get_meta_inf(self, path):
        metadata = {}
        for minion in self.minions:
            metadata.update(minion.get_meta_info(path))
        return metadata
