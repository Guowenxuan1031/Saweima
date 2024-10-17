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

pyautogui.PAUSE=0.02

upgrade_now = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
all_now = [0, 0, 0, 0, 0, 0, 0, 0, 0] 

dayStart = True
lastTenSeconds = False


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
    longclick(0)  #进店
    print("进来")

def start_day():
    pyautogui.moveTo(472, 465, duration=0.15)
    longclick(0)  #开始一天
    print("开始一天")
    
#
#PREPARE

def get_meat_hand_1():
    print("切肉100次")
    if(all_now[3] < 3):
        pyautogui.moveTo(386, 749, duration=0.15)
        pyautogui.mouseDown()  #拿刀
        time.sleep(0.5)
        for i in range(24):   #来回切肉
            pyautogui.moveTo(450, 370, duration=0.1)
            pyautogui.moveTo(450, 600, duration=0.3)
        pyautogui.mouseUp()
        all_now[3] += 8
    
def cut_potato_1():       #长按切薯条
    print("切薯条5秒钟")
    pyautogui.moveTo(1742, 711, duration=0.1)
    longclick(5)
    
def output_potato_1():    #薯条出锅
    print("试图出锅薯条")
    pyautogui.moveTo(1565, 625, duration=0.2)
    longclick(0)
    
def get_all_1():
    
    pyautogui.moveTo(248, 614,duration=0.2)  #点人
    longclick(0)
    
    time.sleep(0.2)
    if(all_now[7] < 2 or all_now[8] < 2):
        time.sleep(0.6)
    if(all_now[4] < 3):
        print("黄瓜！")
        pyautogui.moveTo(412, 539)  #黄瓜
        for i in range(10):
            longclick(0)
        all_now[4] += 8
        
    if(all_now[5] < 3):
        print("盐！")
        pyautogui.moveTo(412, 631)  #盐
        for i in range(10):
            longclick(0)
        all_now[5] += 8
    
    if(upgrade_now[0] == 1):
        if(all_now[7] < 2):
            print("果汁！")
            pyautogui.moveTo(423, 718)  #果汁
            for i in range(5):
                longclick(0)
            all_now[7] = 4
    
    if(upgrade_now[1] == 1):
        if(all_now[8] < 2):
            print("红薯！")
            pyautogui.moveTo(424, 807)  #红薯
            for i in range(9):
                longclick(0)
            all_now[8] = 8
        
    pyautogui.moveTo(248, 614,duration=0.2)  #点人恢复
    longclick(0)

    
def potatochips():    
    if(all_now[6] < 7):
        potatofinish = pyautogui.locateOnScreen('E:\\Saweima\\potatofinish.png', confidence=0.80, region=(1480,634,1670-1480,789-574))
        if(potatofinish != None):
            print("锅中薯条炸制完成！")
            output_potato_1()
            all_now[6] += 6
            cut_potato_1()
        
        
def prepare():
    if(InterruptTime() or InterruptDay()):
        return
    potatochips()
    if(InterruptTime() or InterruptDay() ):
        return
    get_meat_hand_1()
    if(InterruptTime() or InterruptDay()):
        return
    potatochips()
    
    

    
    

# PREPARE END
#
    
# 
# MAKE SAWEIMA
    
    
def make_saweima_pie():
    print("饼皮")
    pyautogui.moveTo(605, 879, duration=0.1)  #饼皮
    longclick(0)

def make_saweima_meat():
    print("肉")
    pyautogui.moveTo(513, 739, duration=0.1)  #肉
    for i in range(3):
        longclick(0)
    all_now[3] -= 1

def make_saweima_cucumber():
    print("黄瓜")
    pyautogui.moveTo(670, 739, duration=0.01)  #黄瓜
    for i in range(3):
        longclick(0)
    all_now[4] -= 1

def make_saweima_salt():
    print("盐")
    pyautogui.moveTo(829, 739, duration=0.01)  #盐
    for i in range(3):
        longclick(0)
    all_now[5] -= 1

def make_saweima_potato():
    print("薯条")
    pyautogui.moveTo(965, 739, duration=0.01)  #薯条
    for i in range(3):
        longclick(0)
    all_now[6] -= 1
        
def make_saweima_roll():
    print("卷饼")
    pyautogui.moveTo(948, 915, duration=0.01)  #卷饼  ??
    pyautogui.mouseDown()
    pyautogui.moveTo(948, 728, duration=0.5)
    pyautogui.mouseUp()
    
def make_saweima_package():
    for i in range(3):
        if(all_now[i] > 0  and  all_now[i] < 10 ):
            print("第" + str(i+1) + "个沙威玛正在装袋")
            pyautogui.moveTo(761, 866, duration=0.1)  #上包装袋
            pyautogui.mouseDown()
            pyautogui.moveTo(1156, 818 + i * 50, duration=0.3)
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
        print("检测到第" + str(i+1) + " 位顾客要沙威玛" + str(len(saweima)) + "个")
        print(saweima)
        customer_now[index][2] = len(saweima)
    
    if(upgrade_now[0] == 1):
        juice = list(pyautogui.locateAllOnScreen('E:\\Saweima\\juice.png', confidence=0.95, region=(703 + index * 300, 370, 869-703, 638-370)) )
        if(len(juice) != 0):
            print("检测到第" + str(i+1) + " 位顾客要果汁" + str(len(juice)) + "个")
            print(juice)
            customer_now[index][4] = len(juice)
            
    if(upgrade_now[1] == 1):
        kebi = list(pyautogui.locateAllOnScreen('E:\\Saweima\\kebi.png', confidence=0.95, region=(703 + index * 300, 370, 869-703, 638-370)) )
        if(len(kebi) != 0):
            print("检测到第" + str(i+1) + " 位顾客要红薯" + str(len(kebi)) + "个")
            print(kebi)
            customer_now[index][7] = len(kebi)
    
                
            
def drag_saweima(index):
    for i in range(3):  # 有就拖动
        if(all_now[i] > 10):
            pyautogui.moveTo(1156, 818 + i * 50)
            pyautogui.mouseDown()
            pyautogui.moveTo(765 + index * 300, 541, duration=0.35)
            pyautogui.mouseUp()
            saweima_lay = pyautogui.locateOnScreen('E:\\Saweima\\saweima_lay.png', confidence=0.90, region=(1060, 792 + i * 50, 1100-1060, 843-792))
            if(saweima_lay == None):
                all_now[i] = 0
                print("第" + str(i+1) + "个沙威玛成功出餐")
                return 1
            
 
    return 0
    
def serve_customer(index):
    # 沙威玛
    for i in range(customer_now[index][2]):
        customer_now[index][2] -= drag_saweima(index)
    if(upgrade_now[0] == 1):
        # 果汁
        for i in range(customer_now[index][4]):
            print("出库一瓶果汁")
            if(all_now[7] > 0):
                pyautogui.moveTo(428, 843)
                pyautogui.mouseDown()
                pyautogui.moveTo(765 + index * 300, 541, duration=0.35)
                pyautogui.mouseUp()
                all_now[7] -= 1
                customer_now[index][4] -= 1
    if(upgrade_now[1] == 1):
        # 红薯
        for i in range(customer_now[index][7]):
            print("出库一个红薯")
            if(all_now[8] > 0):
                pyautogui.moveTo(1184, 700)
                pyautogui.mouseDown()
                pyautogui.moveTo(765 + index * 300, 541, duration=0.35)
                pyautogui.mouseUp()
                all_now[8] -= 1
                customer_now[index][7] -= 1
            
def collect_money():
    print("正在收钱")
    time.sleep(1)
    print("正在收钱")
    pyautogui.moveTo(575, 629, duration=0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(1475, 629, duration=0.7)
    pyautogui.mouseUp()
    
    
def InterruptTime():
    global lastTenSeconds
    timelast = pyautogui.locateOnScreen('E:\\Saweima\\timelast.png', confidence=0.90, region=(218,101,379-218,210-101))
    if(timelast != None):
        print("剩余最后10+s")
        lastTenSeconds = True
        return True

def InterruptDay():
    global dayStart
    dayOver = pyautogui.locateOnScreen('E:\\Saweima\\dayfinish.png', confidence=0.90, region=(857,793,1061-857,975-793))
    menu = pyautogui.locateOnScreen('E:\\Saweima\\menu.png', confidence=0.90, region=(1787,523,1912-1787,733-523))
    if(dayOver != None or menu != None):
        print("检测到今天结束")
        dayStart = True
        pyautogui.moveTo(958, 880, duration=0.3)
        longclick(0)
        time.sleep(3)
        return True
    
    return False

def clear_all():
    global lastTenSeconds
    print("清除全部内容")
    lastTenSeconds = False
    for i in range(len(all_now)):
        all_now[i] = 0
    for i in range( len(customer_now) ):
        for j in range( len(customer_now[0] )):
            customer_now[i][j] = 0
            
def shopping():
    pyautogui.moveTo(888, 679, duration=0.35)
    longclick(0)
    time.sleep(3)
    juice1 = pyautogui.locateOnScreen('E:\\Saweima\\juice1.png', confidence=0.85, region=(465,725,588-465,798-725))
    if(juice1 != None):
        pyautogui.moveTo(434, 860, duration=0.35)
        longclick(0.2)
        pyautogui.moveTo(1054, 528, duration=0.35)
        longclick(0.2)
        print("购买果汁")
        upgrade_now[0] = 1
    kebi1 = pyautogui.locateOnScreen('E:\\Saweima\\kebi1.png', confidence=0.85, region=(1174,597,1282-1174,658-597))
    if(kebi1 != None):
        pyautogui.moveTo(1183, 701, duration=0.35)
        longclick(0)
        pyautogui.moveTo(1054, 528, duration=0.35)
        longclick(0)
        print("购买红薯")
        upgrade_now[1] = 1
    pyautogui.moveTo(1859, 112, duration=0.35)
    longclick(0)
     
        
    
time.sleep(5)  # 切换屏幕

into_shop()





while(True):
    
    if(dayStart == True):
        time.sleep(4)
        shopping()
        time.sleep(5)
        start_day()
        time.sleep(3)
        clear_all()

        cut_potato_1()
        time.sleep(2)
        dayStart = False
    # 初始化准备（预制）
    get_all_1()
    if(lastTenSeconds == False):
        print("------前期准备------")
        prepare() 
        
    if(InterruptDay() ):
        continue
    
    # 没有够就一直做
    print("------制作沙威玛------")
    for i in range(3):
        if(all_now[i] == 0):
            make_saweima()
            
    if(InterruptDay() ):
        continue
    
    # 做完，开始服务
    
    # 扫描顾客状态
    print("------检测顾客状态------")
    for i in range(3):
        scan_customer(i)
        
    print(all_now)
    print(customer_now)
        
    if(InterruptDay() ):
        continue
        
    # 出餐
    print("------出餐------")
    for i in range(3):
        serve_customer(i)
    
    if(InterruptDay() ):
        continue
        
        
    
        
    # 挣钱
    print("------挣钱------")
    collect_money()
    
    if(InterruptDay() ):
        continue
    
    
    
    

    
