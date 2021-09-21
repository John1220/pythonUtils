# -*-coding:utf-8-*-
"""
数据库连接工具 [mysql/postgres]
"""
import os
import configparser
import psycopg2
import pymysql


class ConnectingDatabase(object):
    def __init__(self, database_type):
        self.database_type = database_type
        if self.database_type not in ['mysql', 'postgres']:
            print('当前仅支持: mysql, postgres. 程序终止!')
            exit(0)
        cfg = self.load_para()
        self.host = cfg.get('db', 'host')
        self.port = int(cfg.get('db', 'port'))
        self.user = cfg.get('db', 'user')
        self.pwd = cfg.get('db', 'pwd')
        self.db = cfg.get('db', 'db')

    @staticmethod
    def load_para():
        dir = os.path.dirname(os.path.abspath(__file__))
        cfg_file = dir + '/config.ini'
        cfg = configparser.ConfigParser()
        cfg.read(cfg_file, encoding='gbk')
        return cfg

    def connection_mysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.pwd,
                               db=self.db)
        return conn

    def connection_postgres(self):
        conn = psycopg2.connect(database=self.db, user=self.user, password=self.pwd, host=self.host, port=self.port)
        return conn

    def connection(self):
        if self.database_type == 'mysql':
            conn = self.connection_mysql()
        elif self.database_type == 'postgres':
            conn = self.connection_postgres()
        return conn

    def run_sql(self, sql):
        conn = self.connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

    def get_data(self, sql):
        conn = self.connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        rows = cur.fetchall()
        conn.close()
        return rows
