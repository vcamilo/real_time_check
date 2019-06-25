#! /bin/python

import mysql.connector
import properties as p
from flask import jsonify
import base64

class Closer:
    def __init__(self, closeable):
        self.__closeable = closeable
    def __enter__(self):
        return self.__closeable
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.__closeable.close()
        return False

def con():
    return mysql.connector.connect(
        host = p.db_host,
        user = p.db_user,
        password = base64.b64decode(p.db_password),
        database = p.db_base_name
    )

class Base():
	def show_all(self):
		with Closer(con()) as connection, Closer(connection.cursor()) as cursor:
			cursor.execute("SELECT * FROM {}.MOCK_DATA".format(p.db_base_name))
			rows = cursor.fetchall()
			return rows

	def consulta(self, hostname):
		with Closer(con()) as connection, Closer(connection.cursor()) as cursor:
			cursor.execute(
				"SELECT * FROM {}.MOCK_DATA \
				WHERE hostname LIKE('{}%') LIMIT 10".
				format(p.db_base_name, hostname))
			rows = cursor.fetchall()
			return rows
