import queue
import time
import threading

def producer(queue):
    for i in range(10):
        print(f"producing item {i}")
        queue.put({'name':"sundar"+str(i)})
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()        
        if item is None:
            break        
        print(f"Consumed item {item}")
        time.sleep(1.5)

shared_queue = queue.Queue()

producer_thread = threading.Thread(target=producer,args=(shared_queue,))
consumer_thread = threading.Thread(target=consumer,args=(shared_queue,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
shared_queue.put(None)
consumer_thread.join()

