#!/opt/homebrew/bin/python3
import time
import pyautogui as p

# size
# w x h
WAIT_SEC=120
size = p.size()

# windows button location
h_begin = size.height - 25
w_begin = 25
w_end = w_begin + 750
h_end = h_begin

print(size)
print("begin width:{0} height:{1}".format(w_begin, h_begin))

time.sleep(2)
while True:
    cur_time = time.strftime("%H:%M:%S", time.localtime())
    print("mouse moving " + cur_time )
    p.moveTo(w_begin, h_begin, 1)
    p.click()
    time.sleep(1)
    p.click()
    p.moveTo(w_end, h_end, 1)
    time.sleep(WAIT_SEC)
