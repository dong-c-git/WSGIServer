#coding:utf-8
from pymysql import *

def main():
    conn = connect(host="localhost",port=3306,database='test01',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    for i in range(100000):
        cursor.execute("insert into test_index values ('ha-%d')"%i)
    conn.commit()


if __name__ == '__main__':
    main()