# -*- coding: utf-8 -*-
import os
import pymysql


class DBTool:

    conn = None
    cursor = None

    def __init__(self,conn_dict):
        self.conn = pymysql.connect(host=conn_dict['host'],
                                    port=conn_dict['port'],
                                    user=conn_dict['user'],
                                    passwd=conn_dict['password'],
                                    db=conn_dict['db'],
                                    charset=conn_dict['charset'])
        self.cursor = self.conn.cursor()


    def execute_query(self, sql_string):
        try:
            cursor=self.cursor
            cursor.execute(sql_string)
            list = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return list
        except pymysql.Error as e:
            print("mysql execute error:", e)
            raise

    def execute_noquery(self, sql_string):
        try:
            cursor = self.cursor
            cursor.execute(sql_string)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except pymysql.Error as e:
            print("mysql execute error:", e)
            raise

def main():
    conn_dict = {'host': 'shop.zuoduoduo.cn', 'port': 3306, 'user': 'root', 'password': 'DK900@GBX6W', 'db': 'shop_zuoduoduo_cn', 'charset': 'utf8'}
    conn = DBTool(conn_dict)
    sql_gettables = "select table_name from information_schema.`TABLES` WHERE TABLE_SCHEMA = 'databas_name';"
    list = conn.execute_query(sql_gettables)

    # 文件目标路径，如果不存在，新建一个
    mysql_file_path = 'D:\mysqlscript'
    if not os.path.exists(mysql_file_path):
        os.mkdir(mysql_file_path)

    mysqldump_commad_dict = {'dumpcommad': 'mysqldump --no-data ', 'server': '127.0.0.1', 'user': 'root',
                            'password': 'root', 'port': 3306, 'db': 'shop_zuoduoduo_cn'}

    if list:
        for row in list:
            print(row[0])
            # 切换到新建的文件夹中
            os.chdir(mysql_file_path)
            #表名
            dbtable = row[0]
            #文件名
            exportfile =  row[0] + '.sql'
            # mysqldump 命令
            sqlfromat = "%s -h%s -u%s -p%s -P%s %s %s >%s"
            # 生成相应的sql语句
            sql = (sqlfromat % (mysqldump_commad_dict['dumpcommad'],
                                mysqldump_commad_dict['server'],
                                mysqldump_commad_dict['user'],
                                mysqldump_commad_dict['password'],
                                mysqldump_commad_dict['port'],
                                mysqldump_commad_dict['db'],
                                dbtable,
                                exportfile))
            print(sql)
            result = os.system(sql)
            if result:
                print('export ok')
            else:
                print('export fail')

if __name__ == '__main__':
    main()