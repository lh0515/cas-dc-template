#coding=utf-8
import os,time,datetime

#需定时删除的目录的上一层路径
data_dir="/home/quaiping/code/cas-dc-template/exp-kaggle/ours"


#初始化文件名称列表
dir_name = []
flag = True
split_name2 = 0
#循环取出目录的绝对路径
while(flag):
    for filename in os.listdir(data_dir):
        # print(filename)
        if filename.endswith("pth") and filename != "latest.pth":
            filepath1 = os.path.join(data_dir, filename)
            split_name1 = os.path.split(filepath1)[-1].split('_')[1]
            filepath2 = os.path.join(data_dir, split_name1)
            split_name2 = os.path.split(filepath2)[-1].split('.')[0]
            print(split_name2)
            if(int(split_name2) <= 59):
                if not os.path.exists(filepath1):
                    continue
                print("正在删除文件名为%s的文件"%(filename))
                os.remove(filepath1)
            elif(int(split_name2) > 59):
                break
    if (int(split_name2) > 59):
        flag = False
    #只对目录进行操作，获取目录的最后修改时间，并把最后修改时转换成时间格式
