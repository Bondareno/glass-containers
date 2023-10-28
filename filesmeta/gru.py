class Gru:
    def __init__(self):
        self._minions = []

    def add_minion(self, minion):
        self._minions.append(minion)

    def get_meta_info(self, path):
        metadata = {}
        for minion in self._minions:
            metadata.update(minion.get_meta_info(path))
        return metadata
