import storm.locals as orm

class DataStore(object):
    def __init__(self, url):
        self.store = orm.Store(orm.create_database(url))
    def __enter__(self):
        return self
    def __exit__(self):
        if self.store:
            self.store.close()
        self.store = None

