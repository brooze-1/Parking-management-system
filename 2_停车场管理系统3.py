# 开发时间：2021/6/21  15:48
import time
import datetime
# 导入tkinter库
from tkinter import *

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
        if self.top+1<self.Parking_capacity:
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
        elif self.rear + 1 < self.Capacity_of_access_road:
            self.rear = self.rear + 1
            # 此时self.rear则代表车辆在便道所要停放的位置
            self.Access_road[self.rear] = x


        # 若停车场和便道都已停满，则发出提示
        else:
            print('停车场和便道都已停满,无法再容纳车辆,请换别处停车,请输入“#”退出停车管理系统')
            return


    # 车辆驶出停车场
    def Drive_out(self,car):
        if self.IsEmpty():
            print('此时停车场为空')


        else:
            # if car not in self.s:
            #     car = input(f'停车场中没有车牌号为{car}的车辆，请重新输入：')

            # 将out声明为全局变量
            global out
            # 将要驶出的车辆在停车场的位置储存在out中
            out = self.s.index(car)

            # 记录当前车辆驶出的时间戳
            departure_time = time.time()
            # 将stop_time声明为全局变量
            global stop_time
            # 计算停留时间，用该车辆驶出时间戳减去驶入时间戳，储存在stop_time中
            stop_time = round(departure_time - self.Entry_time[out],2)

            # 换行，并输出当前驶出车辆的驶入时间，驶出时间，停留时间，以及应交纳的停车费
            print(' ')
            print(f'此时驶出停车场是车牌号为{self.s[out]}的车辆,'
                  f'该车驶入时间为{self.datetime_of_entry[out]},'
                  f'驶出时间为{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},'
                  f'停留时长为{stop_time}秒')
            print(f'按照规定收费标准为6元/小时，'
                  f'由于程序上时间较短所以就以秒代替时，'
                  f'故车牌号为{self.s[out]}的车辆所要交纳的停车费用为{round(stop_time*6,1)}元')
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
        date = input('请输入车辆的车牌号（继续输入请按回车,结束请输入“#”）:')
        while date != "#":
            self.Drive_in(date)
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


    def main(self):
        # 创建tkinter对象
        windows = Tk()
        # 设置标题为停车场管理系统
        windows.title('停车场管理系统')
        # 设置窗口大小，注意字母是x
        windows.geometry("400x200")
        # 宽和高都可变（默认是True）
        windows.resizable(width=True, height=True)
        # 创建标签label_1用于显示停车场的容量
        label_1 = Label(windows, text=f'停车场的容车量为：{self.Parking_capacity}', font=('宋体', 10))
        label_1.grid(row=0, column=0,sticky=W)
        # 创建标签label_2用于显示便道上的停车位的容量
        label_2 = Label(windows, text=f'便道容车量为：{self.Capacity_of_access_road}', font=('宋体', 10))
        label_2.grid(row=1, column=0, sticky=W)
        # 创建标签label_3用于显示输入框entry_1前的文字
        label_3 = Label(windows, text='请输入驶入车辆车的牌号:', font=('宋体', 10))
        label_3.grid(row=2, column=0, sticky=W)
        # 创建输入框entry_1用于接收进入停车场的车辆信息
        entry_1 = Entry(windows, width=20)
        entry_1.grid(row=2, column=1, sticky=W)

        # 构建一个get_data_of_drive_in函数用于获取entry_1输入的数据(驶入车辆的数据)
        def get_data_of_drive_in():
            # 获取entry_1的数据（即为车牌号），储存在data_of_entry_1中
            data_of_entry_1 = entry_1.get()
            # 将该车牌号的车驶入停车场
            self.Drive_in(data_of_entry_1)
            print(data_of_entry_1)
            # 清除entry_1中输入的文本内容，便于下一次输入
            entry_1.delete(0, END)
            # 判断停车场以及便道是否都停满了
            if self.top + 1 >= self.Parking_capacity and self.rear + 1 >= self.Capacity_of_access_road:
                # 创建标签label_10用于提示停车场和便道都已停满,无法再容纳车辆
                label_10=Label(windows,text='停车场和便道都已停满,无法再容纳车辆,请换别处停车')
                label_10.grid(row=6,column=0,columnspan=2,sticky=W)
                over()

        # 构建一个get_data_of_drive_out()函数用于获取entry_2输入的数据（驶出车辆的数据）
        def get_data_of_drive_out():
            # 获取entry_2的数据（即为车牌号），储存在data_of_entry_2中
            data_of_entry_2=entry_2.get()

            # 判断要驶出停车场的车的车牌号是否操作self.s中，若不存在则要求重新输入
            if data_of_entry_2 not in self.s:
                # 创建标签label_9用于提示停车场没有车牌号为xxx车辆
                label_9 = Label(windows,text=f'停车场中没有车牌号为{data_of_entry_2}车辆，请重新输入')
                label_9.grid(row=11,column=0,sticky=W)
                # 清除entry_2中输入的文本内容，便于下一次输入
                entry_2.delete(0, END)
            # 将该车牌号的车驶出停车场
            self.Drive_out(data_of_entry_2)
            #  创建标签label_11用于输出当前驶出车辆的驶入时间，驶出时间，停留时间，以及应交纳的停车费
            label_11=Label(windows,text=f'此时驶出停车场是车牌号为{self.s[out-1]}的车辆\n'
                                        f'该车驶入时间为{self.datetime_of_entry[out-1]}\n'
                                        f'驶出时间为{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                                        f'停留时长为{stop_time}秒\n'
                                        f'按照规定收费标准为6元/小时\n'
                                        f'由于程序上时间较短所以就以秒代替时\n'
                                        f'故车牌号为{self.s[out-1]}的车辆所要交纳的停车费用为{round(stop_time*6,1)}元')
            label_11.grid(row=12,column=1,sticky=W)





        # 构建一个over函数用于终止输入,并输出停车场及便道的停车情况
        def over():
            # 获取entry_1的数据（即为车牌号），储存在data_of_entry_1中
            data_of_entry_1 = entry_1.get()
            # 将该车牌号的车驶入停车场
            self.Drive_in(data_of_entry_1)
            # 点击“完成输入”时使得entry_1输入框无法再接收数据
            entry_1.config(state='disabled')
            # 点击“完成输入”时使得button_1输入框无法再接收数据
            button_1.config(state="disabled")
            # 点击“完成输入”时使得button_2输入框无法再接收数据
            button_2.config(state="disabled")
            # 若此时停车场为空,则提示此时停车场为空的信息
            if self.IsEmpty():
                # 创建label_6标签用于输出此时停车场为空的信息
                label_6=Label(windows,text='此时停车场和便道均为空,无车辆信息')
                label_6.grid(row=4,column=0,sticky=W)
            # 若此时停车场不为空，则输出停车场的停车情况
            else:
                # 创建label_4标签用于显示当前停车场的停车状况
                label_4 = Label(windows, text=f'此时停车场状态为:{(self.s)}')
                label_4.grid(row=4,column=0,sticky=W)
                # 若此时便道为空则提示此时便道为空
                if self.acess_isempty():
                    # 创建label_7标签用于输出此时便道为空的信息
                    label_7=Label(windows,text='此时便道为空,无车辆信息')
                    label_7.grid(row=5,column=0,sticky=W)
                # 若此时便道不为空
                else:
                    # 创建label_5标签用于显示当前便道的停车状况
                    label_5=Label(windows,text=f"此时便道的状态为：{self.Access_road}")
                    label_5.grid(row=5, column=0,sticky=W)



        # 设置button_1按钮用于终止输入，并输出停车场及便道的停车情况
        button_1 = Button(windows, text='完成输入', command=over)
        button_1.grid(row=3, column=1, sticky=E)
        # 设置button_1按钮用于输入数据，多次接收驶入车辆的数据，完成交互
        button_2 = Button(windows, text='录入下一辆', command=get_data_of_drive_in)
        # 当停车场和便道都满了的时候就可以使用,state='disabled'加到button的属性当中去，禁止输入
        button_2.grid(row=3, column=1, sticky=W)

        # 创建标签label_8用于显示输入框entry_2前的文字
        label_8 = Label(windows, text='请输入驶出车辆车的牌号:', font=('宋体', 10))
        label_8.grid(row=8, column=0, sticky=W)
        # 创建输入框entry_2用于接收要驶出的车辆的信息
        entry_2=Entry(windows, width=20)
        entry_2.grid(row=8,column=1,sticky=W)
        # 设置button_3按钮用于输入数据，多次接收驶出车辆的数据，完成交互
        button_3=Button(windows,text='确认驶出',command=get_data_of_drive_out)
        button_3.grid(row=9,column=1,sticky=W)
        # 进入主事件循环
        windows.mainloop()

if __name__ == '__main__':
    # 初始化停车场的容量及便道的容量
    p=Parking_management_system(2,3)
    p.main()
    # # 输入每辆车的车牌信息
    # p.Input_vehicle_information()
    # # 输出当前停车场及便道的停车情况
    # p.Output_information()
    # # 随机驶出一辆车，并输出车辆的驶入时间，驶出时间，停留时间以及需交纳的停车费
    # p.Drive_out()
    # # 输出驶出车后的停车场及便道的停车情况
    # p.Output_information()
    # # 再随机驶出一辆车，并输出车辆的驶入时间，驶出时间，停留时间以及需交纳的停车费
    # p.Drive_out()
    # # 输出驶出车后的停车场及便道的停车情况
    # p.Output_information()