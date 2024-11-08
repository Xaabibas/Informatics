import time
from task1 import task1
from task2 import task2
from task3 import task3


start = time.time()
for _ in range(100):
    task1()
end = time.time()
print(end - start)

start = time.time()
for _ in range(100):
    task2()
end = time.time()
print(end - start)

start = time.time()
for _ in range(100):
    task3()
end = time.time()
print(end - start)
