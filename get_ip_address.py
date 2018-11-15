import linecache
import os
import re
import pymysql
import time
import datetime


# 读取行号
def openlinenum():
    num = open('lines_num.log')
    line_num = num.readline()
    if not line_num:
        line_num = 1

    # print(line_num, type(line_num))
    return int(line_num)


# 逐行读取数据
def readuwsgilog(line_num):
    # line_num = openlinenum()
    while True:
        file2 = linecache.getline('uwsgi.log', line_num)
        line_num += 1
        # print(file2)

        if not file2:
            print('读取结束')
            writelinenum(line_num)
            break
        else:
            yield file2


# 记录行号
def writelinenum(num):
    with open('lines_num.log', 'w') as f:
        f.write(str(num))


# 提取信息
def getip(strs):
    patt = re.compile(r'req:.*\d/(\d+).*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.*)\]')

    for data in strs:
        result = patt.findall(data)
        # print(result)
        if result:
            yield result[0]


# 存入数据库
def savemysql(data_tupls):
    conn = pymysql.connect(host='127.0.0.1', db='webvisit', user='dongdong', password='123456', charset='utf8')
    cur = conn.cursor()

    sql = 'insert into ipaddress(num,ip,datatime) VALUES(%s,%s,%s)'
    data = (data_tupls[0], data_tupls[1], data_tupls[2])
    try:
        cur.execute(sql,data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print('error:', e)



# 转换日期格式
def turndata(data):
    # data = 'Wed Nov 14 10:40:36 2018'
    # data = '2018 Nov 14 10:40:36 '
    # res = time.strptime(data, "%Y-%m-%d %H:%M:%S")
    # s1 = time.localtime()
    # print('s1', s1)
    # s2 = time.asctime(s1)
    # print(s2)

    # s3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(s3)

    # '%a %m %d %H:%M:%S %Y'
    # s5 = time.asctime(time.localtime(time.time()))
    # print(s5)

    s6 = time.strptime(data, '%a %b %d %H:%M:%S %Y')
    # print(s6)

    s7 = time.strftime("%Y-%m-%d %H:%M:%S", s6)
    # print('s7',s7)
    return s7


def main():
    # 读取起始行号
    line_num = openlinenum()

    # 读取日志文件
    info = readuwsgilog(line_num)

    # 提取IP
    datas = getip(info)
    for i in datas:
        # print(i)
        pro = (i[0], i[1], turndata(i[2]))
        print(pro)
        savemysql(pro)


if __name__ == "__main__":
    main()
