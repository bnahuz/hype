import peewee
from function import Function

db = peewee.SqliteDatabase('indices-ipca.db')

class Execution(peewee.Model):
    
    function_id = peewee.ForeignKeyField(Function)
    date = peewee.DateField()
    execution_time = peewee.IntegerField()

    class Meta:
        database = db