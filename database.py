import config
import main

from orator import DatabaseManager, Model


class Item(Model):
    __table__ = 'items'


def init_database():
    db = DatabaseManager({
    'mysql': {
        'driver': 'mysql',
        'host': config.MYSQL_ADDR,
        'database': config.MYSQL_DB_NAME,
        'user': config.MYSQL_USER,
        'password': config.MYSQL_PWD,
        'prefix': ''
    }
    })
    Model.set_connection_resolver(db)
    main.db = db
