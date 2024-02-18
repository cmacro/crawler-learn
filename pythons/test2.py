import multiprocessing
import time
import random

# child processs function
def sender(queue, msg):
    # sleep 2~5 seconds, simulate task execution
    time.sleep(random.randint(2,5))
    print(f'sending message {msg}')
    queue.put(msg)

def receiver(queue):
    msg = ''
    while msg != 'closed':
        msg = queue.get()
        print(f'received message: {msg}')
    print('receiver is finished') 

if __name__ == '__main__':
    msgqueue = multiprocessing.Queue()
    # create new child process, 
    sendproc = multiprocessing.Process(target=sender, args=(msgqueue, 'hello'))
    recvproc = multiprocessing.Process(target=receiver, args=(msgqueue,))
    sendproc.start()
    recvproc.start()

    # wait process finsihed
    sendproc.join()
    msgqueue.put('closed')
    recvproc.join()
    print('main process is finished')
    