1. 
* 接收普通类型参数，生成元组参数列表
** 接收keyvalue类型值，生成字典 

2. B

```py
rages = {'美元':6.84, '欧元':8.12, '日元':0.06, '港元':0.88, '澳元':4.98}
def exchange(t, c):
    if t in rages:
        return c * rages[t], 0
    return c, -1

kind = input(r'请输入汇率国：')
amount = float(input(r'请输入兑换额：'))
val, res = exchange(kind, amount)
print(f'{kind} {amount}, 兑换成人民币 {val}元' if res == 0 else f'无效货币，error code: {res}')   
```

## 08-面向对象基础

1. class

2. B

3. 

    class Rect:
        def __init__(self, w, h):
            self.w = w
            self.h = h
        def perimetr(self):
            return (self.w + self.h) * 2
        def area(self):
            return self.w * self.h
        
    r = Rect(10, 20)
    print(f'{r.w}x{r.h}矩形周长：{r.perimetr()}, 面积：{r.area()}')
    r = Rect(5, 5)
    print(f'{r.w}x{r.h}矩形周长：{r.perimetr()}, 面积：{r.area()}')

4.

    class Student:
        def __init__(self, name, age, gender) -> None:
            self.name = name
            self.age = age
            self.gender = gender
        def introduce(self):
            return f'我叫{self.name}, 现在{self.age}, 性别：{self.gender}'

    student1 = Student('夏目',  18, '男')
    print(student1.introduce())


## 09-面向对象深入

1. B，C

2.
1 1 1
1 2 1
1 3 1

3.

    class Rectangle:
        def __init__(self, l, w) -> None:
            self.l = l
            self.w = w
        def area(self):
            return self.l * self.w
        
    class Square(Rectangle):
        def __init__(self, s) -> None:
            super().__init__(s, s)
        def sideLength(self):
            return self.w
        
    square1 = Square(10)
    print(f'正方形的边长：{square1.sideLength()}')


## 10-深入面向对象

1. C
2. ABCD
3.

    class Person:
        def __init__(self, name, age, gender) -> None:
            self.name = name
            self.age = age
            self.gender = gender
    class Student(Person):
        def __init__(self, name, age, gender, score) -> None:
            super().__init__(name, age, gender)
            self.score = score
        def introduce(self):
            return f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 分数: {self.score}"

    student1 = Student('夏目', 18, '男', 99)
    print(student1.introduce())

## 11-迭代器

1. A
2. C
3. A
4. ABC
5.
1
2
1
...
9
3
...
9

## 12-生成器

1. 30,22
2.

    oddNumGenerator = (x for x in range(1, 11) if x % 2 != 0)
    for num in oddNumGenerator: print(num)

3.

    def numGenerator():
        for i in range(1, 11):
            if i not in [3,7,8]:
                yield i
    for val in numGenerator(): print(val)

## 13-闭包装饰器

1. C.6
2. B.15
3.

    def outside(x):
        # outside 函数传入x参数值
        def inside(y):
            # inside 闭包函数传入y参数值，并与outside的x值进行乘法运算返回值
            return x*y
        # outside返回内部引用函数，形成闭包
        return inside
    # 创建一个闭包函数实例
    closure = outside(10)
    # 打印闭包函数计算值
    print(closure(5))
    print(closure(2))

4.

    db = {'admin': '123'}
    # 定义登录装饰器
    def login_required(func):
        # 装饰器函数
        def wrapper():
            # 在 wrapper函数中接受输入用户名和密码
            uid = input(r"请输入用户名：")
            pwd = input(r'请输入密码：')
            # 检查用户名密码是否正确
            if uid in db and db[uid] == pwd:
                # 用户名和密码有效，调用原始函数
                print("登录成功,执行func")
                func()
            else:
                # 验证失败，退出调用原始函数
                print("登录失败")
        # 返回包装后的函数
        return wrapper

    # 使用@login_required对run函数进行装饰
    @login_required
    def run():
        print('函数执行中')
    # 正常调用函数，会执行带装饰函数
    run()

## 14-异常与文件处理

1. C
2. open
3. C
4.

    str_1='d52a733i2327ha244i982d23s553b245'
    letters = []
    for c in str_1:
        try:
            # 触发异常
            int(c)  
        except ValueError:
            letters.append(c)
    print(''.join(letters))

## 15-线程

1. B
2. 线程是进程内的一个执行单元，一个进程能创建的最大线程数量根据OS决定。在多核环境下运行能明显提高程序的并发、响应和资源的利用率。同时提高开发的复杂程度，需要考虑线程间同步通讯，资源竞争死锁等诸多问题。

3.
```py
import threading
import random

class MovieTicket:
    def __init__(self, count) -> None:
        self.count = count
        self.lock = threading.Lock()
    def buy(self, num, id):
        with self.lock:
            if num <= self.count:
                self.count -=num
                print(f'ID:{id} succeed {num}, remaining {self.count}')
                return num
            else:
                print(f'ID:{id} failed insufficient balance, remaining {self.count}')
        return 0
# 购票函数
def purchase(movieticket, numtickets, id):
    movieticket.buy(numtickets, id)
# 创建100张电影票 
movieticket = MovieTicket(100)

# 创建20个线程
threads = []
for i in range(20):
    thread = threading.Thread(target=purchase, args=(movieticket, random.randint(1,10), i))
    threads.append(thread)
# 执行线程
for thread in threads:
    thread.start()
# wait closed
for thread in threads:
    thread.join()

print(f'remaining tickets: {movieticket.count}')
```

## 16-进程

1.
```py
import multiprocessing
import time
import random
# child processs function
def childprocess(id):
    print(f'child process {id} is runing')
    # sleep 2~5 seconds, simulate task execution
    time.sleep(random.randint(2,5))
    print(f'child process {id} is finished')

if __name__ == '__main__':
    # create new child process, 
    proc1 = multiprocessing.Process(target=childprocess, args=(1,))
    proc2 = multiprocessing.Process(target=childprocess, args=(2,))
    proc1.start()
    proc2.start()
    # main process execution
    print("main process is runing")
    # wait process finsihed
    proc1.join()
    proc2.join()
    print('main process is finished')
```

2.
进程：程序执行一次，系统会完整分配独立内存和系统资源，每个进程间不共享内存 
线程：是进程的一个执行单元，多个线程会共享进程内的内存和资源  

- 资源占用： 
- - 进程：大，OS提供 
- - 线程：小，进程提供 
- 通讯：
- - 进程：复杂，系统提供管道、消息队列、共享内存、信号 
- - 线程：简单，共享内存 
- 稳定性：
- - 进程：OS调度，多进程间不影响，除有上下文关系的进程 
- - 线程：进程调度，出现一个线程奔溃会影响所有线程  

3. 写一个进程的之间的通信的代码 
```py
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
```