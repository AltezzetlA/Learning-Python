import time, sys

def stars():
    print(i*' ', end='')
    print('*****')
    time.sleep(0.1)
    
while True:
    for i in range(1,20):
        stars()
    for i in range(19,0,-1):
        stars() 
 
