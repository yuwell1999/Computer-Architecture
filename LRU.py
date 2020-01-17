block_num=4
data_list = []
cache_list= []
cache_order = []
status=""
hitcount=0

data_list = list(map(int, input("请输入访问序列，用空格分开：").split()))
list_len = len(data_list)

print("Cache 0，1，2，3")

for i in range(len(data_list)):
    current=int(data_list[0])
    data_list.remove(current)
    #Cache块未满，不需要置换
    if len(cache_list)<block_num:
        #Cache块装入
        if current not in cache_list:
            cache_list.append(current)
            cache_order.insert(0,current)
            status="装入"
        #Cache块中未满且命中
        elif current in cache_list:
            #把命中元素放到最前面，标记为最新使用
            cache_order.remove(current)
            cache_order.insert(0,current)
            status="命中"
            hitcount += 1

    #Cache块已满，要置换或者命中
    else:
        #Cache块命中
        if current in cache_list:
            # 把命中元素放到最前面，标记为最新使用
            cache_order.remove(current)
            cache_order.insert(0, current)
            status="命中"
            hitcount += 1

        #Cache块未命中，需要置换
        elif current not in cache_list:
            remove_number=cache_order.pop()
            cache_list[cache_list.index(remove_number)]=current
            cache_order.insert(0,current)
            status="置换"

    print("第"+str(i+1)+"次",cache_list,status)

print("缺页率为：",1-(hitcount/list_len))