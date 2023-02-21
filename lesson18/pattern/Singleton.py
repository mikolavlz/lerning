class DB:
    __object = None

    def __init__(self):
        connect = open(...)

    @staticmethod
    def get_object():
        if DB.__object == None:
            DB.__object = DB()
        return DB.__object
    def select(self,query):
        pass
    def delete(self,query):
        pass
    def insert(self,query):
        pass

class Good:
    def __init__(self):
        db = DB.get_object()

    def get_goods(self):
        self.db.select()