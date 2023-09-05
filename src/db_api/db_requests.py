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
        category text, 
        brand text,
        model text,
        parameters text,
        price int,
        photo_intro_path text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_item(self, id:int, category: str, brand: str, model: str, parameters: str, price: int = 0, photo_intro_path: str = ''):
        sql = 'INSERT INTO Items(id, category, brand, model, parameters, price, photo_intro_path) VALUES(?,?,?,?,?,?,?)'
        item_parameters = (id, category, brand, model, parameters, price, photo_intro_path)
        self.execute(sql, item_parameters, commit=True)

    def select_item_info(self, **kwargs)-> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 

    def select_items_info(self, **kwargs)-> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)    

    def select_all_items(self):
        sql = 'SELECT * FROM Items WHERE '
        return self.execute(sql, fetchall=True)
    
    # def get_items_count(self, **kwargs) -> int: # возвращает общее количество всех товаров
    #     sql = 'SELECT * FROM Items'
    #     sql, item_parameters = self.format_args(sql, kwargs)
    #     return len(self.execute(sql, item_parameters, kwargs, fetchall=True))
