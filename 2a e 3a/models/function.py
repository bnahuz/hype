import peewee

db = peewee.SqliteDatabase('acme.db')

class Function(peewee.Model):
    
    function_name = peewee.CharField()
    external_component_avg_latency = peewee.CharField()
    has_external_component = peewee.BooleanField()

    class Meta:
        database = db