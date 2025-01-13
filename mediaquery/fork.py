import os 
import time

r , w = os.pipe()

if (os.fork() == 0):
    print("child Process ID:"+str(os.getpid()))
    while True:
        time.sleep(0.1)
        os.write(w,bytes(input("Send Data to parent: "),'utf-8'))
else:
    print("Parent Process ID:"+str(os.getpid()))
    while True:
        print("Data received: "+str(os.read(r,100),'utf-8'))


