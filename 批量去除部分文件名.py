import os
import win32api


def input_info():
    print("*"*50)
    print("开始删除请输入1：")
    print("更改目录删除请输入2：")
    print("退出请输入3：")
    print("*"*50)


def delete_file_key(dirs, aim):  # 获取目标文件名
    """
    :rtype : object
    
    """
    num = 0
    try:
        for name in os.listdir(dirs):  # 遍历目标文件夹，获得文件夹内所有文件名和文件夹名
            file = dirs + "\\" + name  # 给文件或文件夹名前添加路径
            attr = win32api.GetFileAttributes(file)
            if attr == 16:
                delete_file_key(file, aim)
            elif attr == 32:
                if aim in file:
                    new_name = file.replace(aim, "")
                    num += 1
                    print(num)
                    os.rename(file, new_name)
                    print(new_name)
    except PermissionError as err:
        print("Exception:", err)


def continue_delete():
    name_s = input("请输入去除的内容")
    delete_file_key(input_path, name_s)


# def main():
while True:
    input_info()
    nums = int(input("请输入序号："))
    if nums == 1:
        input_path = input("请输入文件绝对路径：")
        names = input("请输入去除的内容")
        delete_file_key(input_path, names)
        print("目标内容已删除完成！")
    elif nums == 2:
        continue_delete()
        print("目标内容已删除完成！")
    elif nums == 3:
        exit()
    else:
        print("输入错误，请重新输入！")

    # input_path = input("请输入文件绝对路径：")
    # names = input("请输入去除的内容")
    # print("正在删除中……")
    # delete_FileKey(input_path,names)
    #
    # print("目标内容已删除完成！")


# if __name__=="__main__":
#     main()