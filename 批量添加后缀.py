# encoding=utf-8
import os

 
 def opeat():
    # 获取文件夹内所有文件名
    old_names = os.listdir(folder_name_path)
    # 进入目标工作目录操作
    os.chdir(folder_name_path)
    num = 1
    for old_name in old_names:
        full_name = folder_name_path + "\\" + old_name
        if os.path.isdir(full_name):
            pass
        else:
            a = old_name.split(".")
            if a[-1] != "jpg":
                new_name = old_name + "." + names
                print(num)
                os.rename(old_name, new_name)
                num += 1


def main():
    global folder_name_path, names
    folder_name_path = input("请输入目标文件夹路径：")
    names = input("请输入要添加后缀:")
    opeat()
if __name__ == "__main__":
    main()
 