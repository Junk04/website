class DataBase:
    USER = 'db_user'
    PASSWORD = 'db_user'
    PORT = '5432'
    HOST = '172.20.10.5'
    NAME = 'maindb'
    SCHEMA = 'main'
    URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'