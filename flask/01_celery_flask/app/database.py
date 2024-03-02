import mysql.connector
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from flask import Flask
from typing import Any, Callable

from app.exceptions import DoesNotExists


class Database:
    def __init__(self) -> None:
        self._conn: PooledMySQLConnection | MySQLConnectionAbstract | None = None

    def init_app(self, app: Flask) -> None:
        self.__database: str = app.config["DATABASE"]
        self.__username: str = app.config["DB_USERNAME"]
        self.__password: str = app.config["DB_PASSWORD"]
        self.__host: str = app.config["DB_HOST"]
        self.__port: int = int(app.config["DB_PORT"])

    def _create_connection(self) -> None:
        try:
            self._conn = mysql.connector.connect(
                database=self.__database,
                username=self.__username,
                password=self.__password,
                host=self.__host,
                port=self.__port,
            )
            print("-->| Creating Database Connection")
        except Exception as e:
            raise Exception(f"Unable to connect database. {str(e)}")

    def get_conn(self):
        if self._conn is not None:
            return self._conn
        else:
            self._create_connection()
            return self._conn

    def close(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None
            print("-->| Closing Database Connection")

    def save(self):
        if self._conn is not None:
            self._conn.commit()

    @staticmethod
    def _cursor(fn: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(self: "Database", *args: Any, **kwargs: Any):
            conn = self.get_conn()
            cursor = conn.cursor(buffered=True, dictionary=True)
            result = fn(self, cursor, *args, **kwargs)
            cursor.close()
            return result

        return wrapper

    @_cursor
    def post(
        self, cursor: MySQLCursorAbstract, procedure: str, arguments: tuple[Any, ...]
    ):
        print(f"sp | {procedure}")
        try:
            cursor.callproc(procedure, arguments)
        except Exception as e:
            print(f"Hit Query Exception: {str(e)}")
            raise e
        else:
            for row in cursor.stored_results():
                return row.fetchone()

    @_cursor
    def get(
        self, cursor: MySQLCursorAbstract, procedure: str, arguments: tuple[Any, ...]
    ) -> dict[str, Any]:
        print(f"sp | {procedure}")
        try:
            cursor.callproc(procedure, arguments)
        except Exception as e:
            print(f"Hit Query Exception: {str(e)}")
            raise e

        for row in cursor.stored_results():
            if row.rowcount == 0:
                raise DoesNotExists("Record does not exists in the database.")
            return row.fetchone()

    @_cursor
    def put(
        self, cursor: MySQLCursorAbstract, procedure: str, arguments: tuple[Any, ...]
    ) -> None:
        print(f"sp | {procedure}")
        try:
            cursor.callproc(procedure, arguments)
        except Exception as e:
            print(f"Hit Query Exception: {str(e)}")
            raise e
