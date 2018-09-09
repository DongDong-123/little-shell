# encoding=utf-8
import os
import traversefile

# 批量添加后缀名
def add_extend_name(folder_name_path):
    file_name = traversefile.traverse_files(folder_name_path)
    print(file_name)
    for name in file_name:
        print(name)
        new_name = name + "." + extend_name
        print(new_name)
        # old_extend_name = name.split(".")
        # if old_extend_name[-1] == specify_extend:
        #     pass
        # else:
        os.rename(name, new_name)


# def main():
#     add_extend_name(folder_name_path)


folder_name_path = input("请输入目标文件夹路径：")
extend_name = input("请输入要添加后缀:")
add_extend_name(folder_name_path)
# specify_extend = input("请输入要跳过的文件扩展名：")

# if __name__ == "__main__":
#     main()



# 获取目标文件路径，手动输入时可省略该步
# folder_name_path = os.getcwd()
# print(folder_name_path)
# 获取文件夹内所有文件名
# old_names = os.listdir(folder_name_path)
# 进入目标工作目录操作
# os.chdir(folder_name_path)

# 修改文件名
# full_name = folder_name_path + "\\" + old_name


# def opeat():
#     num = 1
#     for old_name in old_names:
#         full_name = folder_name_path + "\\" + old_name
#         if os.path.isdir(full_name):
#             pass
#         else:
#             a = old_name.split(".")
#             if a[-1] != "jpg":
#                 new_name = old_name + "." + names
#                 print(num)
#                 os.rename(old_name, new_name)
#                 num += 1
#
#
# # def file_isdir():
# #     opeat()

