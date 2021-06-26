# 开发时间：2021/6/23  14:27
import time
import datetime

class Parking_management_system(object):
    # 初始化停车场的容量
    def __init__(self,Parking_capacity,Capacity_of_access_road):
        # Parking_capacity为停车场的最大容车数量
        self.Parking_capacity = Parking_capacity
        # 初始化停车场的容量为Parking_capacity,停车场未进车时,将每个停车位初始化为None
        self.s = [None for x in range(0,self.Parking_capacity)]
        # 初始化停车场未停车时,top = -1
        self.top = -1
        # Capacity_of_access_road为便道的最大容车数量
        self.Capacity_of_access_road = Capacity_of_access_road
        # 初始化便道停车容量为Capacity_of_access_road,便道未进车时,将每个停车位初始化为None
        self.Access_road = [None for y in range(self.Capacity_of_access_road)]
        # 初始化便道未停车时,rear = -1
        self.rear = -1


        # 初始化一个self.temp顺序表，用于实现驶出停车场操作时self.s中self.top指针的更改过渡
        self.temp=[]
        # 初始化一个self.temp_of_rear顺序表，用于实现便道车辆驶入停车场操作时，self.Access_road中self.rear指针的更改过渡
        self.temp_of_Access_road = []
        # 初始化self.Entry_time列表，记录车辆进入停车场的时间戳
        self.Entry_time = []
        # 初始化self.datetime_of_entry列表，记录车辆进入停车场的时间
        self.datetime_of_entry = []
        # 初始化self.Departure_time列表，记录车辆驶离停车场的时间
        self.Departure_time = []


    # 判断停车场是否为空
    def IsEmpty(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop


    # 判断便道是否为空
    def acess_isempty(self):
        if self.rear == -1:
            irear = True
        else:
            irear = False
        return irear


    # 车辆进入停车场
    def Drive_in(self,x):
        # 当停车场未停满时
        if self.top+1<self.Parking_capacity and x.isdigit():
            # 使用x.isdigit()来判断x是否为数字
            self.top = self.top + 1
            # 此时self.top则代表车辆在停车场所要停放的位置
            self.s[self.top] = x
            # 记录当前车辆进入的时间戳
            entry_time = time.time()
            # 将车辆进入时间戳存储在self.Entry_time中
            self.Entry_time.append(entry_time)
            # 将车辆进入的时间存储在self.datetime_of_entry中
            self.datetime_of_entry.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


        # 若停车场已经停满,则多余的车辆将停在便道
        elif self.rear + 1 < self.Capacity_of_access_road and x.isdigit():
            # 使用x.isdigit()来判断x是否为数字
            self.rear = self.rear + 1
            # 此时self.rear则代表车辆在便道所要停放的位置
            self.Access_road[self.rear] = x


        # 若停车场和便道都已停满，则发出提示，如果便道都满了则说明停车场和便道都满了
        elif self.rear + 1 == self.Capacity_of_access_road:
            print('停车场和便道都已停满,无法再容纳车辆,请换别处停车,请输入“#”退出停车管理系统')
            return

        # 若输入的车牌号不为数字
        else:
            print('请输入正确的车牌号！！！')
            return


    # 车辆驶出停车场
    def Drive_out(self):
        if self.IsEmpty():
            print('此时停车场为空')


        else:
            # 用car来存储要驶出停车场的车辆的车牌号
            car = input('请输入要驶出停车场的车辆的车牌号：')
            # 判断要驶出停车场的车的车牌号是否操作self.s中，若不存在则要求重新输入
            while car not in self.s:
                car = input(f'停车场中没有车牌号为{car}的车辆，请重新输入：')

            # 将要驶出的车辆在停车场的位置储存在out中
            out = self.s.index(car)
            # 记录当前车辆驶出的时间戳
            departure_time = time.time()
            # 计算停留时间，用该车辆驶出时间戳减去驶入时间戳，储存在stop_time中
            stop_time = round(departure_time - self.Entry_time[out],2)
            # 换行，并输出当前驶出车辆的驶入时间，驶出时间，停留时间，以及应交纳的停车费
            print(' ')
            print(f'此时驶出停车场是车牌号为{self.s[out]}的车辆\n该车驶入时间为{self.datetime_of_entry[out]}\n该车驶出时间为{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n该车停留时长为{stop_time}秒')
            print(f'按照规定收费标准为元/小时，由于程序上时间较短所以就以10秒等价与1小时，故车牌号为{self.s[out]}的车辆所要交纳的停车费用为{round(stop_time*0.3,1)}元')
            print(' ')
            # 该车驶出后删除该车在self.Entry_time中记录的驶入时间
            del self.Entry_time[out]


            # 使用一个for循环语句将self.s中的元素转存到self.temp中
            for i in self.s:
                self.temp.append(i)
            # 在self.temp中删除驶出的车辆
            del self.temp[out]
            # print(self.temp)


            # 重新初始化，将self.top初始化为-1，self.s初始化为空列表
            self.top=-1
            self.s=[None for x in range(0,self.Parking_capacity)]
            # 重新将删除驶出后车辆的self.temp中的元素转存到self.s中完成指针self.top的变换
            for j in self.temp:
                # 当停车场未停满时
                if self.top + 1 < self.Parking_capacity:
                    self.top = self.top + 1
                    # 此时self.top则代表车辆在停车场所要停放的位置
                    self.s[self.top] = j


            # 注意用完了之后一定要重新将self.temp初始化为空列表，方便下次过渡，否则的话就会出问题
            self.temp=[]


            # 判断便道上是否有车
            if self.acess_isempty():
                # 若便道上没有车,则无法从便道向停车场内补充车辆
                return


            else:
                # 若便道上有车,则将便道上的车驶入停车场,直到将停车场填满
                # 将便道上的第一辆车开进停车场中补位
                self.Drive_in(self.Access_road[0])
                # 使用一个for循环语句将self.Access_road中的元素转存到self.temp_of_Access_road中
                for i in self.Access_road:
                    self.temp_of_Access_road.append(i)
                # 在self.temp_of_Access_road中删除驶出的车辆
                del self.temp_of_Access_road[0]
                # 重新初始化，将self.rear初始化为-1，self.Access_road初始化为空列表
                self.rear = -1
                self.Access_road =[None for y in range(self.Capacity_of_access_road)]
                # 重新将删除驶出车辆后的self.temp_of_Access_road中的元素转存到self.Access_road中完成指针self.rear的变换
                for j in self.temp_of_Access_road:
                    if self.rear + 1 < self.Capacity_of_access_road:
                        self.rear = self.rear + 1
                        # 此时self.rear则代表车辆在便道所要停放的位置
                        self.Access_road[self.rear] = j


                # 千万注意使用self.Access_road[self.rear]过渡完后一定要将其初始化为空列表，这样才能方便下次过渡，否则的话结果就会出问题
                self.temp_of_Access_road = []




    # 录入车辆信息
    def Input_vehicle_information(self):
        # 创建一个列表用于存储输入的车牌号判断输入的车牌号是否重复
        temp=[]
        date = input('请输入车辆的车牌号（继续输入请按回车,结束请输入“#”）:')
        while date != "#":
            # 若输入的车牌号没在列表temp中且车牌号为阿拉伯数字，则将该车牌号的车驶入停车场或便道
            if date not in temp and date.isdigit():
                temp.append(date)
                self.Drive_in(date)
                date = input('请输入车辆的车牌号:')
            # 若输入的车牌号(为阿拉伯数字)已存在列表temp中，则提示重新输入
            elif date in temp:
                print(f'车牌号为{date}的车辆已经停好了')
                date = input('请输入车辆的车牌号:')

            # 若输入的车牌号不为阿拉伯数字
            else:
                print('请输入正确的车牌号！！！')
                date = input('请输入车辆的车牌号:')


    # 输出停车场及便道的车辆信息
    def Output_information(self):
        # 判断停车场是否停车
        if self.IsEmpty():
            # 若停车场未停车,则输出此时停车场为空,无车辆信息
            print('此时停车场为空,无车辆信息')
            return
        else:
            # 若停车场有停车,则输出停车场所停放车辆的信息
            print('此时停车场所停放的车辆有:',end=' ')
            for i in range(self.top +1 ):
                print(self.s[i],end = ' ')


            # 判断便道上是否停车
            if self.acess_isempty():
                # 换行
                print(' ')
                # 若便道上未停车则跳出
                print('此时便道为空,无车辆信息')
                return
            else:
                # 若便道上有停车,则输出便道所停放车辆的信息
                print(' ')
                print('此时便道所停放的车辆有:',end=' ')
                for j in range(self.rear+1):
                    print(self.Access_road[j],end=' ')
                # 换行
                print(' ')



if __name__ == '__main__':
    print("*****************************************************")
    print('在该停车场管理系统中，车牌号用阿拉伯数字代替')
    print("*****************************************************")
    # 初始化停车场的容量及便道的容量
    p=Parking_management_system(4,3)
    # 输入每辆车的车牌信息
    p.Input_vehicle_information()
    # 输出当前停车场及便道的停车情况
    p.Output_information()
    # 随机驶出一辆车，并输出车辆的驶入时间，驶出时间，停留时间以及需交纳的停车费
    p.Drive_out()
    # 输出驶出车后的停车场及便道的停车情况
    p.Output_information()
    # 再随机驶出一辆车，并输出车辆的驶入时间，驶出时间，停留时间以及需交纳的停车费
    p.Drive_out()
    # 输出驶出车后的停车场及便道的停车情况
    p.Output_information()

