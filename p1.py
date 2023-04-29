from time import sleep
from threading import Thread

videos = ['DSA', 'OS', 'Networking']

print('Track the git changes11')

class MyThreadClass(Thread):
    
    def __init__(self,value):
        self.value = value
        Thread.__init__(self)
    
    def run(self):
        for vid in videos:
            print(f"{vid} is uploading..,")
            sleep(1)
            print(f"{vid} uploaded successfully.")

t1 = MyThreadClass(10)
t1.start()