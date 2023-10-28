class CommonMinion:
    def get_meta_info(self, path):
        metadata = {
            "size": os.path.getsize(path),
            "created_at": os.path.getctime(path),
            "modified_at": os.path.getmtime(path),
        }
        return metadata
