import pyautogui
import time
import os
import cv2
import numpy as np



for i in range(1000):
    print("---")
    
filenames = os.listdir('E:\\Saweima')
root = 'E:\\Saweima'
print("脚本已启动！")


all_now = [0, 0, 0, 0, 0, 0, 0] 
# 0-2  沙威玛
# 0 无   
#1  有（无包装袋，普通）  
#11  有（有包装袋，普通）
# 3-6  肉，黄瓜，盐，薯条


customer_now = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#  0   -   是否检测到顾客
#  1   -   沙威玛种类
#  2   -   沙威玛个数
#  3   -   薯条个数
#  4   -   软饮个数
#  5   -   橙汁个数
#  6   -   可乐个数
#  7   -   红薯个数

def longclick(time_length):
    pyautogui.mouseDown()
    time.sleep(time_length)
    pyautogui.mouseUp()

def start_game():
    pyautogui.moveTo(1140, 510, duration=0.15)
    longclick(0.5)  #让我们说中文
    time.sleep(2)
    
    pyautogui.moveTo(1718, 953, duration=0.15)
    longclick(0.5)  #开始游戏
    time.sleep(0.5)
    
def into_shop():
    pyautogui.moveTo(973, 737, duration=0.15)
    longclick(0.5)  #进店
    print("进来")

def start_day():
    pyautogui.moveTo(472, 465, duration=0.15)
    longclick(0.5)  #开始一天
    print("开始一天")
    
#
#PREPARE

def get_meat_hand_1():
    print("切肉100次")
    if(all_now[3] < 3):
        pyautogui.moveTo(386, 749, duration=0.15)
        pyautogui.mouseDown()  #拿刀
        time.sleep(0.5)
        for i in range(100):   #来回切肉
            pyautogui.moveTo(450, 395, duration=0.03)
            pyautogui.moveTo(450, 588, duration=0.03)
        pyautogui.mouseUp()
        all_now[3] = 10
    
def cut_potato_1():       #长按切薯条
    print("切薯条5秒钟")
    pyautogui.moveTo(1742, 711, duration=0.1)
    longclick(5)
    
def output_potato_1():    #薯条出锅
    print("试图出锅薯条")
    pyautogui.moveTo(1565, 625, duration=0.1)
    longclick(0.2)
    
def get_all_1():
    
    pyautogui.moveTo(248, 614)  #点人
    longclick(0.1)
    
    if(all_now[4] < 3):
        print("黄瓜！")
        pyautogui.moveTo(412, 539)  #黄瓜
        for i in range(10):
            longclick(0.05)
        all_now[4] = 10
        
    if(all_now[5] < 3):
        print("盐！")
        pyautogui.moveTo(412, 631)  #盐
        for i in range(10):
            longclick(0.05)
        all_now[5] = 10
        
    pyautogui.moveTo(248, 614)  #点人恢复
    longclick(0.1)
    
def potatochips():
    output_potato_1()
    time.sleep(0.5)
    potato = pyautogui.locateOnScreen('E:\\Saweima\\potato.png', confidence=0.90, region=(1480,574,1647-1480,678-574))
    if(potato == None):
        print("没有检测到锅中有薯条！")
        cut_potato_1()
        
        
def prepare():
    potatochips()
    get_meat_hand_1()
    get_all_1()
    potatochips()
    

    
    

# PREPARE END
#
    
# 
# MAKE SAWEIMA
    
    
def make_saweima_pie():
    print("饼皮")
    pyautogui.moveTo(605, 879, duration=0.1)  #饼皮
    longclick(0.1)

def make_saweima_meat():
    print("肉")
    pyautogui.moveTo(513, 739)  #肉
    for i in range(3):
        longclick(0.05)
    all_now[3] -= 1

def make_saweima_cucumber():
    print("黄瓜")
    pyautogui.moveTo(670, 739)  #黄瓜
    for i in range(3):
        longclick(0.05)
    all_now[4] -= 1

def make_saweima_salt():
    print("盐")
    pyautogui.moveTo(829, 739)  #盐
    for i in range(3):
        longclick(0.05)
    all_now[5] -= 1

def make_saweima_potato():
    print("薯条")
    pyautogui.moveTo(965, 739)  #薯条
    for i in range(3):
        longclick(0.05)
    all_now[6] -= 1
        
def make_saweima_roll():
    print("卷饼")
    pyautogui.moveTo(948, 915, duration=0.1)  #卷饼  ??
    pyautogui.mouseDown()
    pyautogui.moveTo(948, 728, duration=0.5)
    pyautogui.mouseUp()
    
def make_saweima_package():
    for i in range(3):
        if(all_now[i] > 0  and  all_now[i] < 10 ):
            print("第" + str(i+1) + "个沙威玛正在装袋")
            pyautogui.moveTo(761, 866)  #上包装袋
            pyautogui.mouseDown()
            pyautogui.moveTo(1156, 818 + i * 50, duration=0.2)
            pyautogui.mouseUp()
            all_now[i] += 10

def make_saweima_numset():
    for i in range(3):
        if(all_now[i] == 0):
            all_now[i] = 1
            break
    
def make_saweima():
    make_saweima_pie()
    
    make_saweima_meat()
    make_saweima_cucumber()
    make_saweima_salt()
    make_saweima_potato()
    
    
    make_saweima_roll()
    
    make_saweima_numset()
    make_saweima_package()
    
    
# MAKE SAWEIMA END
#
    
def scan_customer(index):
    saweima = list(pyautogui.locateAllOnScreen('E:\\Saweima\\saweima.png', confidence=0.95, region=(703 + index * 300, 370, 869-703, 638-370)) )
    if(len(saweima) != 0):
        print("检测到第" + str(i+1) + " 位顾客要沙威玛")
        print(saweima)
        customer_now[index][2] = len(saweima)
    
                
            
def drag_saweima(index):
    for i in range(3):  # 有就拖动
        if(all_now[i] > 10):
            pyautogui.moveTo(1156, 818 + i * 50)
            pyautogui.mouseDown()
            pyautogui.moveTo(765 + index * 300, 541, duration=0.1)
            pyautogui.mouseUp()
            saweima_lay = pyautogui.locateOnScreen('E:\\Saweima\\saweima_lay.png', confidence=0.90, region=(1060, 792 + index * 50, 1100-1060, 843-792))
            if(saweima_lay == None):
                all_now[i] = 0
                print("第" + str(index+1) + "个沙威玛成功出餐")
                return 1
 
    return 0
    
def serve_customer(index):
    # 沙威玛
    for i in range(customer_now[index][2]):
        customer_now[index][2] -= drag_saweima(index)
            
def collect_money():
    print("正在收钱")
    pyautogui.moveTo(600, 629, duration=0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(1884, 629, duration=0.5)
    pyautogui.mouseUp()
    
        
    
time.sleep(5)  # 切换屏幕

into_shop()
time.sleep(5)

start_day()
time.sleep(5)


while(True):
    # 初始化准备（预制）
    print("------前期准备------")
    prepare() 
    
    # 没有够就一直做
    print("------制作沙威玛------")
    for i in range(3):
        if(all_now[i] == 0):
            make_saweima()
    
    # 做完，开始服务
    
    # 扫描顾客状态
    print("------检测顾客状态------")
    for i in range(3):
        scan_customer(i)
        
    # 出餐
    print("------出餐------")
    for i in range(3):
        serve_customer(i)
        
    # 挣钱
    print("------挣钱------")
    collect_money()

    
