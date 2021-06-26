# 开发时间：2021/6/20  21:52
# 导入tkinter库
from tkinter import *
# 创建tkinter对象
windows=Tk()
# 设置标题
windows.title('')
# 设置窗口大小，注意字母是x
windows.geometry("400x200")
# 宽和高都可变（默认是True）
windows.resizable(width=True,height=True)
# 创建标签label_1用于显示当前停车场的空余停车位
label_1 = Label(windows,text=f'当前停车场的空余停车位数量为：{4}',font=('宋体',10))
label_1.grid(row=0,column=0)
# 创建标签label_2用于显示当前便道上的空余停车位
label_2=Label(windows,text=f'当前便道的空余停车位数量为：{4}',font=('宋体',10))
label_2.grid(row=1,column=0,sticky=W)
# 创建标签label_3用于显示输入框前的文字
label_3=Label(windows,text='请输入驶入车辆车的牌号:',font=('宋体',10))
label_3.grid(row=2,column=0,sticky=W)
# 创建输入框用于接收进入停车场的车辆信息
entry_1 = Entry(windows,text='0',width=20)
entry_1.grid(row=2,column=1,sticky=W)
# 构建一个get_data函数用于获取entry_1输入的数据
def get_data():

    # 获取entry_1的数据，储存在data_of_entry_1中
    data_of_entry_1 = entry_1.get()
    print(data_of_entry_1)
    # 清除entry_1中输入的文本内容，便于下一次输入
    entry_1.delete(0, END)
def over():
    entry_1.config(state='disabled')
    label_4=Label(windows,text=f'此时停车场所停放的车辆有:')


button_1 = Button(windows,text='完成输入',command=over)
button_1.grid(row=3,column=1,sticky=E)
button_2=Button(windows,text='录入下一辆',command=get_data)
# 当停车场和便道都满了的时候就可以使用,state='disabled'加到button的属性当中去，禁止输入
button_2.grid(row=3,column=1,sticky=W)
# 进入主事件循环
windows.mainloop()

