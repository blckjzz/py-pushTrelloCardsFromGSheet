import peewee
from petition import Petition
from log import Log


if __name__ == '__main__':
    try:
        Petition.drop_table()
        Petition.create_table()
        Log.drop_table()
        Log.create_table()
    except peewee.OperationalError:
        print 'Tabela Petition ja existe!'