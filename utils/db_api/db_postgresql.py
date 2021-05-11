import asyncio
import asyncpg
from data.config import PGUSER, PGPASSWORD, ip, DATABASEE

class Database:
    
    def __init__(self, pool):
        self.pool = pool

    @classmethod
    async def create(cls):
        pool = await asyncpg.create_pool(
            user=PGUSER,
            password=PGPASSWORD,
            host=ip,
            database=DATABASEE
        )
        return cls(pool)
    
    async def create_table_users(self):
        #Обратим внимание, что ошибку с тем, что такая база уже существует
        #Мы сразу обрабатываем тут в запросе
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id INT NOT NULL,
        Name VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        PRIMARY KEY (id))
        """
        await self.pool.execute(sql)

    @staticmethod
    #Обратим внимания что у @statickmethod нет аргумента self
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parametrs, start=1)
        ])
        return sql, tuple(parametrs.values())

    async def add_user(self, id: int, Name: str, email: str = None):
        sql = "INSERT INTO Users (id, name, email) VALUES ($1, $2, $3)"
        try:  
            await self.pool.execute(sql, id, Name, email)
        except asyncpg.exceptions.UniqueViolationError:
            pass

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        #Метод featch возвращает все строки которые нам вернёт база данных
        #И в данном случае, она вернёт всю таблицу
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parametrs = self.format_args(sql, kwargs)
        #Тоже отличие от того как мы работали с SQLite, там параметры передавались именованые
        #Тут же мы их передаём просто в распаковоном виде, ПЕРЕДАДУТСЯ СПИСКОМ
        return await self.pool.fetchrow(sql, *parametrs)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.pool.fetchval(sql)

    async def update_user_email(self, email, id):
        sql = "UPDATE Users SET email = $1 WHERE id = $2"
        return await self.pool.execute(sql, email, id)

    async def delete_users(self):
        sql = "DELETE FROM Users WHERE True"
        return await self.pool.execute(sql)

#Так происходит подключение к бд
#db = Database(loop=asyncio.get_event_loop())