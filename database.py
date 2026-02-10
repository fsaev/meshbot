from ZODB import FileStorage, DB
from persistent import Persistent

class MeshBotDB(Persistent):
    def __init__(self, db_path='defaults.fs'):
        self.db_path = db_path
        self.storage = FileStorage.FileStorage(self.db_path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()
        self.idx = self.get_index()

    def save_data(self, key, value):
        self.root[key] = value
        self.idx += 1
        self.root['index'] = self.idx
        self.connection.commit()

    def get_index(self):
        return self.root.get('index', 0)

    def load_data(self, key):
        return self.root.get(key, None)
    
    def load_all_data(self):
        return dict(self.root)

    def close(self):
        self.connection.close()
        self.db.close()