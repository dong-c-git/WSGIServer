#coding:utf-8
from pymysql import *


def main():
    conn = connect(host='localhost',port=3306,database='test01',user='root',password='root',charset='utf8')
    cs1 = conn.cursor()

    # # 非安全的方式
    # # 输入 " or 1=1 or "   (双引号也要输入)
    # find_name = '"or 1=1 or"'
    # sql = 'select * from goods where name="%s"' % find_name
    # print("""sql===>%s<====""" % sql)
    # # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs1.execute(sql)
    # print(count)
    #安全方式：
    # 构造参数列表
    find_name = '"or 1=1 or"'
    params = [find_name]
    # 执行select语句，并返回受影响的行数：查询所有数据
    count = cs1.execute('select * from goods where name=%s', params)
    
    # 注意：
    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可

    # 打印受影响的行数
    print(count)
    result = cs1.fetchall()
    print(result)

    conn.commit()
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()
