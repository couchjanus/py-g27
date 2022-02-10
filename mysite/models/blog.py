from libs.database import Database
DB = './storages/blog.db'

class Blog(object):
    def __init__(self):
        self._db = Database(DB)
        
    def new(self, data):
        self._db.save('blogs', 'title, category, cover, content', data)
        
    def all(self):
        return self._db.get('blogs', ('*'))
    
    def get(self, id):
        return self._db.getById('blogs', id)
    
    def remove(self, id):
        return self._db.delete('blogs', id)
