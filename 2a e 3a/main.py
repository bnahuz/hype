import peewee
from models.execution import Execution
from models.function import Function

if __name__ == '__main__':

    try:
        Execution.create_table()
        Function.create_table()
    except peewee.OperationalError:
        print ('Tabela já existe!')