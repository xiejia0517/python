import pymysql
import csv
import codecs
rootPath = "F:/Python/csv/"
def get_conn():
    db = pymysql.connect(host="shop.zuoduoduo.cn",port=3306,
                         user="root",password="DK900@GBX6W",
                         db="shop_zuoduoduo_cn",charset="utf8")
    return db

def execute_all(cursor,sql,args):
    cursor.execute(sql,args)
    return cursor.fetchall()

def list_table(db):
    cursor = db.cursor()
    cursor.execute("show tables")
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    
    return table_list
def domain():
    db = get_conn()
    tablist = list_table(db)
    for res in tablist:
        print(res)
        red_mysql_to_csv(res,db)
    db.close()
def red_mysql_to_csv(tabName,db):
    tabpath = rootPath+tabName+".csv";
    print(tabpath)
    with codecs.open(filename=tabpath,mode='w',encoding='utf-8')as f:
        write = csv.writer(f,dialect='excel')
        cursor =db.cursor()
        sql ='select * from '+tabName
        results = execute_all(cursor=cursor,sql=sql,args=None)
        
        for res in results:
            print(res)
            write.writerow(res)
        

if __name__ == '__main__':
    domain()
