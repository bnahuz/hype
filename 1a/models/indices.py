import peewee

db = peewee.SqliteDatabase('indices-ipca.db')

class Ipca(peewee.Model):
    
    anomes = peewee.CharField()
    indice = peewee.FloatField()

    class Meta:
        database = db