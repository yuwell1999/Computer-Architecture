t12 = 25
t34 = 150
t5 = 800
t = [25,25,150,150,800]
queue = [0, 0, 0, 0, 0, 0, 0]


def check():
    flag = False
    for i in range(1, 6):
        if queue[i] == 1:
            print(str(i) + ",", end="")
            flag = True

    if flag:
        print("号设备在请求队列中")


tt1 = tt2 = tt3 = tt4 = tt5 = 0
tt=[0,0,0,0,0]

for i in range(1, 6):
    queue[i] = 1

for time in range(10, 1000, 10):
    if queue[1] == 0:
        if time >= tt1 + t12:
            queue[1] = 1

    if queue[2] == 0:
        if time >= tt2 + t12:
            queue[2] = 1

    if queue[3] == 0:
        if time >= tt3 + t34:
            queue[3] = 1

    if queue[4] == 0:
        if time >= tt4 + t34:
            queue[4] = 1

    if queue[5] == 0:
        if time >= tt5 + t5:
            queue[5] = 1

    # for j in range(6):
    #     if queue[j]==0:
    #         if time >= tt[j]+t[j]:
    #             queue[j]=1
    #
    # for j in range(6):
    #     if queue[j]==1:
    #         pass
    if queue[1] == 1:
        print(str(time) + "us时刻服务1号设备 ", end="")
        tt1 = time
        queue[1] = 0
        check()
        continue

    if queue[2] == 1:
        print(str(time) + "us时刻服务2号设备 ", end="")
        tt2 = time
        queue[2] = 0
        check()
        continue

    if queue[3] == 1:
        print(str(time) + "us时刻服务3号设备 ", end="")
        tt3 = time
        queue[3] = 0
        check()
        continue

    if queue[4] == 1:
        print(str(time) + "us时刻服务4号设备 ", end="")
        tt4 = time
        queue[4] = 0
        check()
        continue

    if queue[5] == 1:
        print(str(time) + "us时刻服务5号设备 ", end="")
        tt5 = time
        queue[5] = 0
        check()
        continue
