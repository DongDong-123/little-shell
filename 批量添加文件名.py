#只适用于文件数小于10的，大于10 ，需原文件名前有首位为0的序号，
import os
file_path = input("请输入文件所在路径：")
add_name = input("请输入要添加的内容：")
old_names = os.listdir(file_path)
os.chdir(file_path)
num = 1
for name in old_names:
    new_name = str(num)+add_name+name
    os.rename(name,new_name)
    num += 1
    print(new_name)