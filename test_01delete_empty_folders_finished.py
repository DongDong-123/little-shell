import os
import traverse


def delete_empty_folder(dirs):
    num = 0
    try:
        list_name = traverse.traverse_folders(dirs)  # 调用自定义模块
        for name in list_name:
            if len(os.listdir(name)) == 0:  # 判断是否为空文件夹
                # print(name)
                # os.rmdir(name)  # 删除空文件夹
                os.removedirs(name)  # 递归删除空文件夹
                num += 1
                print("第%d个空文件夹:%s已删除" % (num, name))  # 打印删除结果
    except PermissionError as err:
        print("Exception:", err)


def main():
    input_path = input("请输入文件绝对路径：")
    os.chdir(input_path)
    print("正在删除中……")
    delete_empty_folder(input_path)
    print("空文件夹删除完成！")


if __name__ == "__main__":
    main()
