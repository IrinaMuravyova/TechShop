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

# таблица пользователей
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

 # таблица всех товаров товаров
    def create_table_items(self):
        sql="""
        CREATE TABLE Items(
        id int NOT NULL,
        category_id int, 
        brand_id int,
        model_id int,
        parameters text,
        price int,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)
    

    def create_table_category(self):
        sql="""
        CREATE TABLE Category(
        id int NOT NULL,
        category text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)


    def create_table_brand(self):
        sql="""
        CREATE TABLE Brand(
        id int NOT NULL,
        id_category int,
        brand text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)
    
    def create_table_model(self):
        sql="""
        CREATE TABLE Model(
        id int NOT NULL,
        id_brand int,
        model text,
        photo_path text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_item(self, id:int, category_id: str, brand_id: str, model_id: str, parameters: str, price: int = 0):
        sql = 'INSERT INTO Items(id, category_id, brand_id, model_id, parameters, price) VALUES(?,?,?,?,?,?)'
        item_parameters = (id, category_id, brand_id, model_id, parameters, price)
        self.execute(sql, item_parameters, commit=True)

    def add_category(self, id:int, category: str):
        sql = 'INSERT INTO Category(id, category) VALUES(?,?)'
        parameters = (id, category)
        self.execute(sql, parameters, commit=True)
    
    def add_brand(self, id:int, id_category:int, brand: str):
        sql = 'INSERT INTO Brand(id, id_category, brand) VALUES(?,?,?)'
        parameters = (id, id_category, brand)
        self.execute(sql, parameters, commit=True)

    def add_model(self, id:int, id_brand: int, model: str, photo_path: str=''):
        sql = 'INSERT INTO Model(id, id_brand, model, photo_path) VALUES(?,?,?,?)'
        parameters = (id, id_brand, model, photo_path)
        self.execute(sql, parameters, commit=True)
    
    def get_category_name(self, **kwargs)-> list:
        sql = 'SELECT category FROM Category WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 
    
    def get_brand_name(self, **kwargs)-> list:
        sql = 'SELECT brand FROM Brand WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 
    
    def get_model_name(self, **kwargs)-> list:
        sql = 'SELECT model FROM Model WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 
    
    def get_model_id(self, **kwargs)-> list:
        sql = 'SELECT id FROM Model WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 
    
    def get_photo_path(self, **kwargs)-> list:
        sql = 'SELECT photo_path FROM Model WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 

    def select_item_info(self, **kwargs)-> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True) 

    def select_items_info(self, table, **kwargs)-> list:
        sql = f'SELECT * FROM {table} WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)    

    def select_all_items(self, table):
        sql = f'SELECT * FROM {table} WHERE '
        return self.execute(sql, fetchall=True)
    
    def get_items_count(self, table, **kwargs) -> int: # возвращает общее количество всех товаров
        sql = f'SELECT * FROM {table} WHERE '
        sql, item_parameters = self.format_args(sql, kwargs)
        return len(self.execute(sql, item_parameters, kwargs, fetchall=True))
