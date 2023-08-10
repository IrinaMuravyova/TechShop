import sqlite3

class Database:
    def __init__(self, db_path: str = 'shop_database.db'):
        self.db_path = db_path
    
    @property # взаимодействуем с подключением как со свойством
    def connection(self):
        return sqlite3.connect(self.db_path)
    
    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data=cursor.fetchall()
        connection.close()
        return data
    #TODO: сделать это асинхронно через серверную БД

    def create_table_users(self):
        sql="""
        CREATE TABLE Users(
        id int NOT NULL,
        phone text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    
    @staticmethod
    def format_args(sql, parameters: dict)-> tuple: # аккуратно формируем sql команду с параметрами, чтобы случайно на их место не передать никакие функции
        sql += ' AND '.join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())
    
    def create_table_items(self):
        sql="""
        CREATE TABLE Items(
        id int NOT NULL,
        name text,
        count int,
        photo_path text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)
