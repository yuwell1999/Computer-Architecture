import numpy as np

block_num=4
data_list = []
cache_list = []
#cache_order = []
status=""
hitcount=0

data_list = list(map(int, input("请输入访问序列，用空格分开：").split()))
list_len = len(data_list)
counter=np.zeros(list_len)

for i in range(list_len):
    counter[i]=-1

for i in range(list_len):
    if counter[i]<block_num and counter[i]!=-1:
        counter[i] += 1
        if i not in cache_list:
            cache_list.append(i)



print("Cache 0，1，2，3")
print("第"+str(i+1)+"次",cache_list,status)

print("缺页率为：",1-(hitcount/list_len))