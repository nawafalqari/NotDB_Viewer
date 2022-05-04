from notdb import NotDBClient

db = NotDBClient('t.ndb', password='123')

db.appendMany([{'name': 'Nawaf'} for i in range(10)])